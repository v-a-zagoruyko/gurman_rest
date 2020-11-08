from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^tour/', Tour, name='tour'),
    url(r'^menu/', MainMenu, name='main_menu'),
]