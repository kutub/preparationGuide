from rest_framework import serializers

from study.models import Syllabus, Lesson, Reading


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'reading_name', 'description')


class LessonDetailSerializer(serializers.ModelSerializer):
    lessons = ReadingListSerializer(many=True)

    class Meta:
        model = Lesson
        fields = [
            'lesson_name',
            'lessons'
        ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'lesson_name',
            'description',
        )


class SyllabusSerializer(serializers.ModelSerializer):
    subject_list = LessonSerializer(many=True)

    class Meta:
        model = Syllabus
        fields = (
            'subject',
            'description',
            'subject_list'
        )


