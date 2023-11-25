from django import forms
from .models import ContactUs


class MessageForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تماس'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام'
        })
    )

    class Meta:
        model = ContactUs
        fields = ['name', 'phone_number', 'message']