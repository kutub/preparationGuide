# Generated by Django 2.1.2 on 2018-10-17 12:22

from django.conf import settings
from django.db import migrations, models
import mcq.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMcq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=200, unique=True)),
                ('batch_year', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(mcq.models.get_sentinel_user), related_name='mcq_batch_updated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='McqLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=200, unique=True)),
                ('number_for_subject', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='McqSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, unique=True)),
                ('number_for_subject', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(mcq.models.get_sentinel_user), related_name='updated_subject_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mcqlesson',
            name='lesson_for',
            field=models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), related_name='belongs_to_subject', to='mcq.McqSubject'),
        ),
        migrations.AddField(
            model_name='mcqlesson',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(mcq.models.get_sentinel_user), related_name='mcq_updated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allmcq',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(mcq.models.get_sentinel_user), related_name='lessons', to='mcq.Batch'),
        ),
        migrations.AddField(
            model_name='allmcq',
            name='created_by',
            field=models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allmcq',
            name='lesson',
            field=models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), related_name='lessons', to='mcq.McqLesson'),
        ),
        migrations.AddField(
            model_name='allmcq',
            name='subject',
            field=models.ForeignKey(on_delete=models.SET(mcq.models.get_sentinel_user), related_name='subjects', to='mcq.McqSubject'),
        ),
        migrations.AddField(
            model_name='allmcq',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(mcq.models.get_sentinel_user), related_name='allmcq_updated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]