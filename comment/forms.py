from django import forms
from django.forms import ModelForm
from .models import Comment

class comment_form(ModelForm):
    """
    A form for collecting user information
    """

    class Meta:
        model = Comment
        fields = ["content"]
