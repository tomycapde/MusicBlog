from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','body','image','category']
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'body': 'Cuerpo',
            'image': 'Imagen',
            'category': 'Categoria'
        }


