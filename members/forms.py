from django import forms


class user_form(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=50)
    lastname = forms.CharField(label="Last Name", max_length=50)
    age = forms.IntegerField(label="Age")
    phone = forms.IntegerField(label="Phone number")

