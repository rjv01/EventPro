from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields=['name','regno','mno','email','eventname']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'regno', 'upi_id', 'transaction_id', 'payment_screenshot']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name1','email1','subject1','message1']
