from django import forms

from .models import Syllabus

class StatusForm(forms.ModelForm):

    class Meta:
        model = Syllabus

        fields = [
            'subject',
            'description'
        ]