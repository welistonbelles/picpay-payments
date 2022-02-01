from django import forms

class DonationForm(forms.Form):
    value = forms.DecimalField(label="Valor", decimal_places=2, max_digits=8)