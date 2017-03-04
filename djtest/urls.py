from django.conf.urls import url
from django.contrib import admin

from core import views as core_views
from authentication import views as auth_views
from testing import views as test_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^signup/$', auth_views.sign_up, name='sign_up'),
    url(r'^signin/$', auth_views.sign_in, name='sign_in'),
    url(r'^signout/$', auth_views.sign_out, name='sign_out'),
    url(r'^test_details/(?P<pk>[0-9]+)/$',
        test_views.test_details, name='test_details'),
    url(r'^test/(?P<pk>[0-9]+)/$',
        test_views.test_page, name='test_page'),
    url(r'^test/(?P<pk>[0-9]+)/get_questions/$',
        test_views.get_questions, name='get_questions'),
    url(r'^test/(?P<pk>[0-9]+)/result/$',
        test_views.result, name='result'),
]
