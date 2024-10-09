"""
Provides a form for views at view.py
"""
from django import forms
from django.forms import ModelForm
from .models import Post

class blog_form(ModelForm):
    """
    A form for collecting user information
    """

    class Meta:
        model = Post
        fields = ["title", "content", "status"]
