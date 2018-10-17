from django.urls import path

from .views import AllMcqCategory, McqDetailView

urlpatterns = [
    path('', AllMcqCategory.as_view(), name='mcq_subject_list'),
    path('lesson/<lesson>/', McqDetailView.as_view(), name='mcq_detail'),
]