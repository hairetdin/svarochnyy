from django import forms
from django.forms import ModelForm, Textarea

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=Textarea(attrs={'cols': 40, 'rows': 10}), max_length=250)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)