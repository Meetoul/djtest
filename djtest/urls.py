from django.conf.urls import url
from django.contrib import admin

from core import views as core_views
from authentication import views as auth_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^signup/$', auth_views.sign_up, name='sign_up'),
    url(r'^signin/$', auth_views.sign_in, name='sign_in'),
    url(r'^signout/$', auth_views.sign_out, name='sign_out'),
]
