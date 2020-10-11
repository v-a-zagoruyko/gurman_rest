from django.shortcuts import render
from .models import *


def index(request):
    menu = Menu.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'index.html', context=context)
