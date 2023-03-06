from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['type', 'full_name', 'phone', 'email', 'address', 'postal_code', 'way_to_get']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Ф.И.О*'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Телефон*'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Почта*'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Адрес'
            }),
            'postal_code': forms.TextInput(attrs={
                'placeholder': 'Почтовый индекс'
            }),

            'type': forms.Select(choices=(('Физ.лицо', 'Физическое лицо'),
                                          ('Юр.лицо', 'Юридическое лицо'))),
            'way_to_get': forms.Select(choices=(('Самовывоз', 'Самовывоз с г. Гатчина ул. Рысева 62А'),
                                                ('Доставка по СПб', 'Доставка по г. Санкт-Петербург'),
                                                ('ТК', 'Доставка до ТК')))
        }
