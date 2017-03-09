from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Test


def test_details(request, pk):
    test = get_object_or_404(Test, pk=pk)
    context = {
        'test': test,
    }
    return render(request, 'testing/test_details.html', context)


def test_page(request, pk):
    if not request.user.is_authenticated:
        raise Http404
    test = get_object_or_404(Test, pk=pk)
    questions = Test.objects.get(pk=pk).question_set.all()
    questions = [
        {
            'id': q.pk,
            'text': q.text,
            'choices': [
                {
                    'id': c.pk,
                    'text': c.text
                } for c in q.choice_set.all()]
        } for q in questions]
    context = {
        'test': test,
        'questions': questions
    }
    return render(request, 'testing/test_page.html', context)


def get_questions(request, pk):
    questions = Test.objects.get(pk=pk).question_set.all()
    response = [
        {
            'id': q.pk,
            'text': q.text,
            'choices': [
                {
                    'id': c.pk,
                    'text': c.text
                } for c in q.choice_set.all()]
        } for q in questions]
    return JsonResponse({'questions': response})


def result(request, pk):
    print(request.POST)
    return HttpResponseRedirect(reverse('home'))
    # answers = json.loads(request.GET['answers'])
    # print(answers)
    # test = Test.objects.get(pk=pk)
    # questions = test.question_set.all()
    # test.passes_number += 1
    # test.save()
    # correct_answers = {
    #     str(q.pk): str([
    #         c.pk for c in q.choice_set.all() if c.correct
    #     ][0]) for q in questions
    # }
    # num_of_correct = 0
    # for k, v in answers.items():
    #     if correct_answers[k] == v:
    #         num_of_correct += 1
    # percentage = int(num_of_correct / len(answers) * 100)
    # context = {
    #     'percentage': percentage,
    # }
    # return render(request, 'testing/test_result.html', context)
