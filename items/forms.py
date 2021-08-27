from django import forms
from .models import Symbol


class AddSymbolForm(forms.ModelForm):
    class Meta:
        model = Symbol
        fields = [
            'name',
        ]


class UpdateSymbolForm(forms.ModelForm):
    class Meta:
        model = Symbol
        fields = [
            'name',

        ]
