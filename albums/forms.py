from .models import Categorie, Album, modelClient, Software
from django import forms
from django.forms.widgets import ClearableFileInput

class AlbumCreateForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'photos': ClearableFileInput(attrs={
                'multiple': True,
            })
        }