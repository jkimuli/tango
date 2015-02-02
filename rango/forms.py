__author__ = 'julius'

from django import forms
from .models import Page,Category

class CategoryForm(forms.ModelForm):
    name = forms.