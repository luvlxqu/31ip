from django import forms
from .models import User

class UserForm(forms.ModelForm):
    model = Userfields = ['login', 'password', 'first_name', 'last_name', 'age']
    labels = {
        'login':'Логин',
        'password': 'Пароль',
        'first_name': 'Имя',
        'last_name' : 'Фамилия',
        'age' :'Возраст',
    }