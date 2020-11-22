from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^tour/', Tour, name='tour'),
    url(r'^menu/', MainMenu, name='main_menu'),
    url(r'^new-year-menu/', NewYearMenu, name='new_year_menu'),
    url(r'^delivery-menu/', DeliveryMenu, name='delivery_menu'),
    url(r'^сaucasus-menu/', CaucasusMenu, name='сaucasus_menu'),
]