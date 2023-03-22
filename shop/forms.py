from .models import User_Request
from django import forms

class User_RequestForm(forms.ModelForm):
    class Meta:

        model = User_Request
        fields = ['full_name', 'company', 'position', 'email', 'phone', 'subject', 'text']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': '*ФИО',
                'data-no-numbers': True,
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Название организации',
                'id': 'text_input'
            }),
            'position': forms.TextInput(attrs={
                'placeholder': 'Должность',
                'data-no-numbers': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Почта'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder':'*Телефон',
                'id':'user_phone_input',
                'class':'phone_number',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': '*Тема сообщения'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': '*Сообщение'
            })
        }
