from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Test


def test_page(request, pk):
    test = get_object_or_404(Test, pk=pk)
    context = {
        'test': test,
    }
    return render(request, 'testing/test.html', context)


def question(request):
    test_pk = request.GET['test_id']
    question_pk = request.GET['question_id']
    try:
        question = Test.objects.get(
            pk=test_pk).question_set.get(pk=question_pk)
        choices = Test.objects.get(
            pk=test_pk).question_set.get(pk=question_pk).choice_set.all()
        response = {
            'text': question.text,
            'choices': [{'text': x.text, 'id': x.pk} for x in list(choices)],
        }
        return JsonResponse(response)
    except:
        return HttpResponse('-1')
