from django import forms

class filepath(forms.Form):
    path_name = forms.CharField(max_length=100)
