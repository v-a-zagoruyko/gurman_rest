from django.shortcuts import render
from .models import *


def Index(request):
    return render(request, 'index.html', context={})

def Tour(request):
    return render(request, 'tour.html', context={})

def MainMenu(request):
    specimen = MenuSpecimen.objects.get(title='Меню')

    context = {
        'specimen': specimen,
        'menu': Menu.objects.filter(specimen=specimen).order_by('kind'),
    }

    return render(request, 'menu.html', context=context)

def NewYearMenu(request):
    specimen = MenuSpecimen.objects.get(title='Новогоднее меню')

    context = {
        'specimen': specimen,
        'menu': Menu.objects.filter(specimen=specimen).order_by('kind'),
    }

    return render(request, 'menu.html', context=context)

def CaucasusMenu(request):
    specimen = MenuSpecimen.objects.get(title='Кавказская кухня')

    context = {
        'specimen': specimen,
        'menu': Menu.objects.filter(specimen=specimen).order_by('kind'),
    }

    return render(request, 'card_menu.html', context=context)

def DeliveryMenu(request):
    specimen = MenuSpecimen.objects.get(title='На вынос')

    context = {
        'specimen': specimen,
        'menu': Menu.objects.filter(specimen=specimen).order_by('kind'),
    }

    return render(request, 'menu.html', context=context)
