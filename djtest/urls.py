from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'},
        name='login'),
]
