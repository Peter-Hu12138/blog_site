"""
Provides a form for views at view.py
"""
from django import forms


class user_form(forms.Form):
    """
    A form for collecting user information
    """
    user_name = forms.CharField(label="User name", max_length=50)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput)
