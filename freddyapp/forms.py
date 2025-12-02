from django import forms
from .models import Animatronic

class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned', 'parties']
        
        widgets = {
            'build_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'parties': forms.CheckboxSelectMultiple(),
        }


        error_messages = {
            'name': {
                'required': "The name of the animatronic is required",
                'max_length': "The name of the animatronic must not be more than 50 characters long",
            },
            'build_date': {
                'required': "The build date is required",
            },
        }