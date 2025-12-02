from django import forms
from .models import Animatronic

# Formulario para crear y editar animatrónicos
class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned', 'parties']
        
        # Personalización de widgets
        widgets = {
            'build_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'parties': forms.CheckboxSelectMultiple(),
        }

        # Mensajes de error personalizados
        error_messages = {
            'name': {
                'required': "The name of the animatronic is required",
                'max_length': "The name of the animatronic must not be more than 50 characters long",
            },
            'build_date': {
                'required': "The build date is required",
            },
        }
        