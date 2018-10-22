from .models import Neighbourhood,Profile,Business
from django import forms

class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['admin']
