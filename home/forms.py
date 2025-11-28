from django import forms
from .models import ContactModelForm


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'contact-name form-control',
            'placeholder': 'نام خود را وارد کنید',
        }),
        max_length=20,
        required=True
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'contact-message form-control',
            'placeholder': 'پیام خود را وارد کنید',
            'rows': 4,
        }),
        max_length=500,
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'contact-email form-control',
            'placeholder': 'email@example.com',
        }),
        required=False
    )

    class Meta:
        model = ContactModelForm
        fields = ['name', 'email', 'text']
