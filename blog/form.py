from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'body']

        labels = {
            'title': '제목',
            'image': '이미지',
            'body': '내용'
        }