from django import forms

class Message_Form(forms.Form):
    receiver = forms.CharField(max_length=200, label="Para:")
    subject = forms.CharField(max_length=200, label="Asunto:")
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':10, 'cols':50}), label="Mensaje:")

class Respond_Form(forms.Form):
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':10, 'cols':50}), label="Mensaje:")