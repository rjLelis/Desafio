from django import forms
from .models import Planilha

class PlanilhaForm(forms.ModelForm):

    class Meta():
        model = Planilha
        fields = ['nome', 'cliente', 'arquivo']
