from django import forms
from .models import Monitoring, Client


class MonitoringForm(forms.Form):

    CONDITION_CHOICES = [
        ('լավ', 'լավ'),
        ('վատ', 'վատ'),
        ('գերազանց', 'գերազանց')
    ]

    client = forms.ModelChoiceField(
        label='Ընտրեք գործընկեր', limit_choices_to=1, required=False, queryset=Client.objects.all())
    condition = forms.ChoiceField(choices=CONDITION_CHOICES,
                                  required=False, label='Ընտրեք գնահատական')
    details = forms.CharField(widget=forms.Textarea,
                              required=False, label='Մեկնաբանություն')
