from django import forms
from .models import *
from django.forms import  ModelForm


class PostForm(forms.ModelForm):
    title = forms.CharField(label = 'Title',widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Posts
        fields = ['title', 'content', 'image']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',

            })
        }


