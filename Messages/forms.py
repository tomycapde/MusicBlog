from django import forms

class Message_Form(forms.Form):
    receiver = forms.CharField(max_length=200)
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':10, 'cols':50}))
    