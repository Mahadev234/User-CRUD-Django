from django import forms


class AddForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="First Name",
        max_length=50,
        required=True,
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Last Name",
        max_length=50,
        required=True,
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        label="Contact Information",
    )

class UpdateForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="First Name",
        max_length=50,
        required=True,
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Last Name",
        max_length=50,
        required=True,
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        label="Contact Information",
    )