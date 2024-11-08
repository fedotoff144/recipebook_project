from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Users, Recipe


class UsersCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'class': 'field', 'placeholder': 'Имя пользователя (username)'}))
    password1 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'field', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Users
        fields = ('username', 'password1', 'password2')


class UsersAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'class': 'field', 'placeholder': 'Имя пользователя (username)'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'field', 'placeholder': 'Пароль'}))

    class Meta:
        model = Users


class UsersProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=100, label='',
                                 widget=forms.TextInput(
                                     attrs={'class': 'personal-field', 'placeholder': 'Имя'}))
    last_name = forms.CharField(required=False, max_length=100, label='',
                                widget=forms.TextInput(
                                    attrs={'class': 'personal-field', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                 attrs={'class': 'personal-field', 'placeholder': 'E-mail'}))
    gender = forms.ChoiceField(label='', choices=[('M', 'Мужчина'), ('F', 'Женщина'), ],
                               widget=forms.RadioSelect(
                                   attrs={'class': 'radio-button'}))
    birthday = forms.DateField(required=False, label='',
                               widget=forms.DateInput(
                                   attrs={'class': 'personal-field', 'placeholder': 'Дата рождения', 'type': 'date'}))
    image = forms.ImageField(required=False, label='',
                             widget=forms.FileInput(
                                 attrs={'class': 'personal-field', 'placeholder': 'Ваше фото'}))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'birthday', 'image', 'gender']


class RecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(required=True, label='', max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'recipe-name', 'placeholder': 'Название рецепта'}))
    servings = forms.IntegerField(required=True, label='Количество порций', min_value=1, max_value=100,
                                  widget=forms.NumberInput(
                                      attrs={'class': 'main-info-field'}))
    time = forms.IntegerField(required=True, label='Время приготовления', min_value=5, max_value=500,
                              widget=forms.NumberInput(
                                  attrs={'class': 'main-info-field'}))
    ingredients = forms.CharField(required=True, label='',
                                  widget=forms.Textarea(
                                      attrs={'class': 'big-text', 'placeholder': 'Ингридиенты'}))
    cooking_steps = forms.CharField(required=True, label='',
                                    widget=forms.Textarea(
                                        attrs={'class': 'big-text', 'placeholder': 'Пошаговая инструкция'}))
    description = forms.CharField(required=True, label='', max_length=200,
                                  widget=forms.Textarea(
                                      attrs={'class': 'small-text', 'placeholder': 'Описание рецепта'}))
    image = forms.ImageField(required=False, label='',
                             widget=forms.FileInput(
                                 attrs={'placeholder': 'Описание рецепта'}))

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'servings', 'time', 'description', 'ingredients', 'cooking_steps',
                  'image', 'category']
