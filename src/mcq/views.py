from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import McqSubject, McqLesson, AllMcq


class AllMcqCategory(ListView):
    model = McqSubject


class McqDetailView(ListView):
    model = AllMcq

    def get_queryset(self):
        self.lesson = get_object_or_404(McqLesson, lesson_name=self.kwargs['lesson'])
        return AllMcq.objects.filter(lesson=self.lesson)
