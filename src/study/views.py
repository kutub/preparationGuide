from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Syllabus, Lesson, Reading
from study.api.serializers import (
    SyllabusSerializer,
    LessonSerializer,
    ReadingListSerializer,
    LessonDetailSerializer
)


class SubjectListApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Syllabus.objects.all()
        serializer = SyllabusSerializer(qs, many=True)
        return Response(serializer.data)


class LessonDetailApiView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class ReadingDetailApiView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Reading.objects.all()
    serializer_class = ReadingListSerializer


class StudyView(ListView):
    model = Syllabus


class LessonListView(ListView):
    template_name = 'study/lesson_by_subject.html'

    def get_queryset(self):
        self.syllabus = get_object_or_404(Syllabus, subject=self.kwargs['subject'])

        return Lesson.objects.filter(lesson_for=self.syllabus)

class ReadingListView(ListView):
    template_name = 'study/reading_by_lesson.html'

    def get_queryset(self):
        self.lesson = get_object_or_404(Lesson, lesson_name=self.kwargs['lesson'])
        print(self.lesson)
        return Reading.objects.filter(reading_for=self.lesson)


class ReadingDetailView(DetailView):
    model = Reading

    def get_context_data(self, *args, **kwargs):
        context = super(ReadingDetailView, self).get_context_data(*args, **kwargs)
        return context
