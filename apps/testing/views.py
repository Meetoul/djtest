from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Test


def test_details(request, pk):
    test = get_object_or_404(Test, pk=pk)
    context = {
        'test': test,
    }
    return render(request, 'testing/test_details.html', context)


@login_required
def test_page(request, pk):
    test = get_object_or_404(Test, pk=pk)
    context = {
        'test': test
    }
    return render(request, 'testing/test_page.html', context)


def test_result(request, pk):
    user_answers = request.POST.dict()
    user_answers.pop('csrfmiddlewaretoken')
    test = Test.objects.get(pk=pk)
    questions = test.question_set.all()
    correct_answers = {str(q.pk): str(q.choice_set.get(
        correct=True).pk) for q in questions}
    res_per_question = []
    for key, val in correct_answers.items():
        res_per_question.append(
            (questions.get(pk=key), user_answers[key] == val))
    number_of_correct = sum(1 for x in res_per_question if x[1])
    percentage = round(number_of_correct / len(res_per_question) * 100, 1)
    context = {
        'test': test,
        'percentage': percentage,
        'res_per_question': res_per_question,
    }
    return render(request, 'testing/test_result.html', context)
