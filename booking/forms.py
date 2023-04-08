from django import forms
from .models import slot


class slotForm(forms.ModelForm):
    class Meta:
        model = slot
        fields = ['customer', 'server', 'date', 'time']
