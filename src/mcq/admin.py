from django.contrib import admin

# Register your models here.

from .models import McqSubject, McqLesson, Batch, AllMcq

@admin.register(McqSubject, McqLesson, Batch, AllMcq)
class McqAdmin(admin.ModelAdmin):
    class Meta:
        model = McqSubject

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        obj.save()
