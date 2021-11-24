from django import forms
from django.core.validators import EmailValidator

class GifForm(forms.Form):
    title = forms.CharField(max_length=10)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length=5,
        label="Uploader",

        help_text='Must contain al least 8 characters',
        error_messages={'required': 'Please enter a valid email address', 'max_length': 'thats way too much brosef'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-md'})
    )
    field_order = ['uploader_name', 'title', 'url']


