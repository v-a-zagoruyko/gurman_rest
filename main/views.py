from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *


def Index(request):
    return render(request, 'index.html', context={})

def Tour(request):
    return render(request, 'tour.html', context={})

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        code = context.get('code')
        specimen = MenuSpecimen.objects.get(code=code)
        menu = Menu.objects.filter(specimen=specimen).order_by('category', 'title')

        context.update({
            'title': specimen.title,
            'menu': menu,
        })

        return self.render_to_response(context)

class MenuSpecialView(TemplateView):
    template_name = 'menu_special.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        code = context.get('code')
        specimen = MenuSpecimen.objects.get(code=code)
        menu = Menu.objects.filter(specimen=specimen).order_by('category', 'title')

        context.update({
            'title': specimen.title,
            'menu': menu,
        })

        return self.render_to_response(context)
