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
        'menu': Menu.objects.filter(specimen=specimen),
    }

    return render(request, 'menu.html', context=context)