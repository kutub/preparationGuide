from django.shortcuts import render

from django.views.generic.base import TemplateView
from study.models import Reading


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_reading'] = Reading.objects.all()[:2]
        print(context['latest_reading'])
        return context