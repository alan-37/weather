from django import forms

class MyForm(forms.Form):
    city = forms.CharField(max_length=255,label='Город')