from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Users(AbstractUser):
    gender = models.CharField(max_length=1, verbose_name='пол')
    birthday = models.DateField(blank=True, null=True, verbose_name='дата рождения')
    image = models.ImageField(upload_to='users_images/', blank=True, null=True, verbose_name='фото пользователя')

    def __str__(self):
        return f'username: {self.username}, email: {self.email}'

    class Meta:
        verbose_name = 'Пользователи'


class RecipeCategory(models.Model):
    category = models.CharField(max_length=100, verbose_name='категория')
    name = models.CharField(max_length=100, verbose_name='имя категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория рецептов'


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, verbose_name='название рецепта')
    servings = models.PositiveSmallIntegerField(blank=False, verbose_name='количество порций')
    time = models.PositiveSmallIntegerField(blank=False, verbose_name='время приготовления')
    description = models.TextField(verbose_name='описание')
    ingredients = models.TextField(verbose_name='ингредиенты')
    cooking_steps = models.TextField(verbose_name='шаги приготовления')
    image = models.ImageField(upload_to='recipes_photo/', blank=True, verbose_name='фото рецепта')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Recipe(pk={self.pk}, '
                f'recipe: {self.recipe_name!r}, '
                f'user: {self.user.username}, '
                f'category: {self.category.name!r})')

    class Meta:
        verbose_name = 'Рецепт'
