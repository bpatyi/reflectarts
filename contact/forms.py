from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,)
    email = forms.EmailField()
    location = forms.CharField(max_length=128)
    comment = forms.CharField(widget=forms.Textarea,)
