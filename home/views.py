from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Info,Services


class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['info'] = Info.objects.all()
        context['service'] = Services.objects.all()
        return context
