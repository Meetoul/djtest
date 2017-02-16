from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import RegistrationForm
from .models import TestUser


def register(request):
    user = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            new_user = User.objects.create_user(
                username=information.get('username'),
                password=information.get('password'),
                email=information.get('email')
            )
            new_user.save()
            forumUser = TestUser(user=new_user)
            forumUser.save()
            user = new_user

            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegistrationForm()

    context = {'form': form,
               'user': user
               }
    return render(request, 'authentication/register.html', context)
