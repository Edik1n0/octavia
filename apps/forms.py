from django import forms

class CarritoForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())