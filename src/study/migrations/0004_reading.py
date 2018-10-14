# Generated by Django 2.1.2 on 2018-10-12 19:38

from django.conf import settings
from django.db import migrations, models
import study.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0003_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_name', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET(study.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('reading_for', models.ForeignKey(on_delete=models.SET(study.models.get_sentinel_user), related_name='belongs_to_lesson', to='study.Lesson')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(study.models.get_sentinel_user), related_name='updated_reading_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]