from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class McqSubject(models.Model):
    subject = models.CharField(max_length=200, unique=True)
    number_for_subject = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='updated_subject_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)
    def __str__(self):
        return self.subject


class McqLesson(models.Model):
    lesson_name = models.CharField(max_length=200, unique=True)
    lesson_for = models.ForeignKey(McqSubject,
                                   related_name='belongs_to_subject',
                                   on_delete=models.SET(get_sentinel_user))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='mcq_updated_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)
    number_for_subject = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.lesson_name


class Batch(models.Model):
    batch_name = models.CharField(max_length=200, unique=True)
    batch_year = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='mcq_batch_updated_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.batch_name


class AllMcq(models.Model):
    question = models.CharField(max_length=255, unique=True)
    s1 = models.CharField(max_length=120, null=True, blank=True)
    s2 = models.CharField(max_length=120, null=True, blank=True)
    s3 = models.CharField(max_length=120, null=True, blank=True)
    s4 = models.CharField(max_length=120, null=True, blank=True)
    # choice_list = ArrayField(models.CharField(max_length=200), size=4, blank=True)
    # batch_tags = ArrayField(models.CharField(max_length=200), blank=True)
    answer = models.CharField(max_length=120)
    subject = models.ForeignKey(McqSubject,
                                   related_name='subjects',
                                   on_delete=models.SET(get_sentinel_user))
    lesson = models.ForeignKey(McqLesson,
                                   related_name='lessons',
                                   on_delete=models.SET(get_sentinel_user))
    batch = models.ForeignKey(Batch,
                                   related_name='lessons',
                                   on_delete=models.SET(get_sentinel_user), blank=True, null=True,)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='allmcq_updated_user',
                                   on_delete=models.SET(get_sentinel_user),
                                   null=True, blank=True)

    def __str__(self):
        return self.question