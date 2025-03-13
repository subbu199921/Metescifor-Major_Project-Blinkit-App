from django import forms
from django.contrib.auth.forms import UserCreationForm,User
from .models import Vendor

class VendorRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'contact_number', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Vendor.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                contact_number=self.cleaned_data['contact_number'],
                address=self.cleaned_data['address']
            )
        return user