from django.conf.urls import url
from django.contrib import admin

from core import views as core_views
from authentication import views as auth_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^register/$', auth_views.register, name='register'),
]
