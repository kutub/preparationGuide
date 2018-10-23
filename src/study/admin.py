from django.contrib import admin

# Register your models here.

from .models import Syllabus, Lesson, Reading
from .forms import StatusForm

@admin.register(Syllabus, Lesson, Reading)
class SyllabusAdmin(admin.ModelAdmin):

    # list_display = ['subject', 'description']

    class Meta:
        model = Syllabus

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        obj.save()


# admin.site.register(Syllabus, Syllabus)Admin
