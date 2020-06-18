from django import forms
from .models import Client
from fertilizers.models import Fertilizer


class CalculationForm(forms.Form):

    TYPE_CHOICES = [
        ('grape_main', 'Grape Main'),
        ('grape_simple', 'Grape Simple'),
        ('potato', 'Potato')
    ]

    client = forms.ModelChoiceField(
        label='Ընտրեք գործընկեր', limit_choices_to=1, required=False, queryset=Client.objects.all())

    area = forms.DecimalField(min_value=0, required=False,
                              decimal_places=2, label='Մուտքագրեք այգու չափերը', initial=0.00)
    group_type = forms.ChoiceField(
        choices=TYPE_CHOICES, initial='grape_main', required=False, label='Ընտրեք տիպը',)


class SaleFretilizerForm(forms.Form):
    client = forms.ModelChoiceField(
        label='Ընտրեք գործընկեր', limit_choices_to=1, required=False, queryset=Client.objects.all())
    fertilizer = forms.ModelChoiceField(
        label='Ընտրեք պարարտանյութ', required=False, queryset=Fertilizer.objects.all())
    sale_qty = forms.DecimalField(min_value=0, required=False,
                                  decimal_places=2, label='Նշեք քանակը', initial=0.00)
