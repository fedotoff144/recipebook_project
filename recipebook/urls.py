from django.urls import path

from recipebook.views import home, register, user_logout, user_login, rules, help_view, \
    advertisement, profile, categories_preview, recipes_category, add_recipe, recipe_detail, edit_recipe

app_name = 'recipebook'

urlpatterns = [
    path('', home, name='home'),
    path('rules/', rules, name='rules'),
    path('ad/', advertisement, name='advertisement'),
    path('help/', help_view, name='help_template'),

    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', profile, name='profile'),
    path('categories/', categories_preview, name='categories'),
    path('recipes_category/<int:category>/', recipes_category, name='recipes_category'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/edit/', edit_recipe, name='edit_recipe'),
]
