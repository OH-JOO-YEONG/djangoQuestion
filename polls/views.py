from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
# from .forms import NameForm

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(
        request,
        'polls/index.html',
        context
    )

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #Question 모델클래스로부터 pk=question_id 검색 조건에 맞는 객체를 조회합니다.
    return render(
        request,
        'polls/detail.html',
        {'question': question},
    )


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        'polls/results.html',
        {'question': question},
    )

# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#
#         if form.is_valid():
#             new_name = form.cleaned_data['name']
#             return  HttpResponseRedirect('/thanks/')
#
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})