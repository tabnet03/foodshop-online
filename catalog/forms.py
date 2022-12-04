from django import forms


class Calcform(forms.Form):
    son1 = forms.CharField()
    son2 = forms.CharField()
    op = forms.ChoiceField(choices=(
        ('+', 'Plus'),
        ('-', 'Minus')
    ))
    img = forms.ImageField()

    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # phone = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)
