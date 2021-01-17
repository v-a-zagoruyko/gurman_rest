from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^tour/', Tour, name='tour'),
    path('menu/<str:code>/', MenuView.as_view(), name='menu'),
    path('menu-special/<str:code>/', MenuSpecialView.as_view(), name='menu_special'),
]