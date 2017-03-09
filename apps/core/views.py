from django.shortcuts import render

from testing.models import Test


def home(request):

    tests = Test.objects.order_by('passes_number')
    return render(request, 'core/home.html', {'tests': tests})
