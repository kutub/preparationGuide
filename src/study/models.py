from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Syllabus(models.Model):
    subject = models.CharField(max_length=200, unique=True)
    number_for_subject = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='updated_syllabus_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)

    objects = StatusManager()

    def __str__(self):
        return self.subject


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200, unique=True)
    lesson_for = models.ForeignKey(Syllabus,
                                   related_name='subject_list',
                                   on_delete=models.SET(get_sentinel_user))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='updated_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)
    number_for_subject = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.lesson_name


class Reading(models.Model):
    reading_name = models.CharField(max_length=300, unique=True)
    # reading_teaser = models.CharField(max_length=320, unique=True)
    description = RichTextField(null=True, blank=True)
    reading_for = models.ForeignKey(Lesson,
                                   related_name='lessons',
                                   on_delete=models.SET(get_sentinel_user))
    reading_for_subject = models.ForeignKey(Syllabus,
                                   related_name='readings',
                                   on_delete=models.SET(get_sentinel_user))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='updated_reading_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)

    def __str__(self):
        return self.reading_name