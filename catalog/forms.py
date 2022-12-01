from django import forms


class Cform(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)