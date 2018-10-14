from django.urls import path

from .views import StudyView, LessonListView, ReadingListView, ReadingDetailView

urlpatterns = [
    path('', StudyView.as_view(), name='syllabus_list'),
    path('subject/<subject>/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<lesson>/', ReadingListView.as_view(), name='reading_list'),
    path('reading/<int:pk>/', ReadingDetailView.as_view(), name='reading-detail'),
]