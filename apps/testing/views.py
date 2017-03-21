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
    num_of_correct = 0
    for key, val in correct_answers.items():
        if user_answers[key] == val:
            num_of_correct += 1
    percentage = round((num_of_correct / len(correct_answers)) * 100, 1)
    print(percentage)
    context = {
        'test': test,
        'percentage': percentage,
    }
    return render(request, 'testing/test_result.html', context)
