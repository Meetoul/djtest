from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import TestUser


def sign_up(request):
    user = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            new_user = User.objects.create_user(
                username=information.get('username'),
                password=information.get('password'),
                email=information.get('email'),
            )
            new_user.save()
            forumUser = TestUser(user=new_user)
            forumUser.save()
            user = new_user

            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm()

    context = {'form': form,
               'user': user,
               }
    return render(request, 'authentication/register.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            user = authenticate(username=information.get('username'),
                                password=information.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = SignInForm()
        user = None

    context = {'form': form}

    return render(request, 'authentication/login.html', context)


@login_required()
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
