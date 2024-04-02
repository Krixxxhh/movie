#builtin form
from django import forms
from app.models import Movie

class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"