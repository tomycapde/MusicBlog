from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class PostForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = RichTextField(config_name='description')
    body = RichTextField(config_name='default')
    #image = forms.ImageField(upload_to="uploads/")
    category = forms.CharField(max_length=50)
    