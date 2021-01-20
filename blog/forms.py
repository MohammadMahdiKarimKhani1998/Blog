from django import forms
from blog.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}), }
