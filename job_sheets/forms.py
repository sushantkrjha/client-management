from django import forms
from .models import JobSheet

class JobSheetForm(forms.ModelForm):
    class Meta:
        model = JobSheet
        fields = '__all__'
        widgets = {
            'received_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
