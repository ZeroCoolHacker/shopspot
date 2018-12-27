from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from accounts.models import User

class BuyerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user

class SellerSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        return user

