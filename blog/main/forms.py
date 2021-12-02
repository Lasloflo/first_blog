from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content', 'post')
        widgets = {'post': forms.HiddenInput}  #  поле скрывается, потому что передается автоматически


class RegisterUserForm(UserCreationForm): #  форма для регистрации
    # прописываются стили для полей и др. атрибуты. Через класс мета стили не подключаются
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form_row'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form_row'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_row'}))
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(attrs={'class': 'form_row'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # для формы для вывода на странице
        # widgets = {
        #    'username': forms.TextInput(attrs={'class': 'form_row'}),
        #    'password1': forms.PasswordInput(attrs={'class': 'form_row'}),
        #    'password2': forms.PasswordInput(attrs={'class': 'form_row'})
        #}


class LoginUserForm(AuthenticationForm):  # форма для входа на сайт

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form_row'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_row'}))
    # если нужны доп поля то можно прописать в этой форме

