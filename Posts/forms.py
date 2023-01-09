from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','body','author' ,'image','category']
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'body': 'Cuerpo',
            'author': 'Autor',
            'image': 'Imagen',
            'category': 'Categoria'
        }


