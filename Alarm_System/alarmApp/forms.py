from django import forms
from .models import Alarm

class AlarmEvent(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ['title', 'description', 'start_date', 'end_date', 'time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'maxlength': '20'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'description',
                'maxlength': '50'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'start-date'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'end-date'
            }),
            
            'time': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'form-control'
            }),
        }