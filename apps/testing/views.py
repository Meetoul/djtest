from django.shortcuts import render, get_object_or_404

from .models import Test


def test_page(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = Test.objects.get(pk=pk).question_set.all()
    context = {
        'test': test,
        'questions': questions,
    }
    return render(request, 'testing/test_detail.html', context)
