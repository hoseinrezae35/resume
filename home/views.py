from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .models import Info, Services, Portfolio
from .forms import ContactForm


class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['info'] = Info.objects.all()
        context['service'] = Services.objects.all()
        context['Portfolio'] = Portfolio.objects.all()
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app:home')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
