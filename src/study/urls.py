from django.urls import path

from .views import (
    StudyView,
    LessonListView,
    ReadingListView,
    ReadingDetailView,

    SubjectListApiView,
    LessonDetailApiView,
    ReadingDetailApiView
)

urlpatterns = [
    path('api/', SubjectListApiView.as_view(), name='subject_list'),
    path('api/lesson/<int:pk>/', LessonDetailApiView.as_view(), name='lesson_list'),
    path('api/reading/<int:pk>/', ReadingDetailApiView.as_view(), name='reading-detail'),

    path('', StudyView.as_view(), name='index'),
    path('subject/<subject>/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<lesson>/', ReadingListView.as_view(), name='reading_list'),
    path('reading/<int:pk>/', ReadingDetailView.as_view(), name='reading-detail'),
    ]