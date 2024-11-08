import random
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Recipe, Users, RecipeCategory
from .forms import RecipeForm, UsersCreationForm, UsersAuthenticationForm, UsersProfileForm


# Create your views here.

def home(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, 'recipebook/home.html', {'recipes': random_recipes})


def advertisement(request: HttpRequest):
    return render(request, 'recipebook/advertisement.html')


def help_view(request):
    return render(request, 'recipebook/help.html')


@login_required(login_url='/login/')
def rules(request):
    return render(request, 'recipebook/rules.html')


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients_raw = recipe.ingredients.replace('\r', '').split('\n')
    ingredients = dict(map(lambda x: x.split(':'), ingredients_raw))
    steps = recipe.cooking_steps.replace('\r', '').split('\n')
    return render(request, 'recipebook/recipe_detail.html',
                  {'recipe': recipe, 'ingredients': ingredients, 'steps': steps})


def categories_preview(request):
    return render(request, 'recipebook/recipe_categories.html')


def recipes_category(request, category):
    recipes = Recipe.objects.filter(category=category)
    category_name = RecipeCategory.objects.get(pk=category).name
    return render(request, 'recipebook/recipe_category.html', {'recipes': recipes, 'category_name': category_name})


@login_required(login_url='/login/')
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            if not form.cleaned_data['image']:
                recipe.image = 'recipes_photo/default_recipe.jpg'
            recipe.user = request.user
            recipe.save()
            return redirect('recipebook:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipebook/add_recipe.html', {'form': form})


# handle adding recipe without image and delete old image before saving new
@login_required(login_url='/login/')
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            if not form.cleaned_data['image']:
                recipe.image = 'recipes_photo/default_recipe.jpg'
            recipe.save()
            return redirect('recipebook:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipebook/edit_recipe.html', {'form': form, 'recipe': recipe})


def register(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipebook:home')
    else:
        form = UsersCreationForm()
    return render(request, 'recipebook/register.html', {'form': form})


@login_required(login_url='/login/')
def profile(request):
    user = get_object_or_404(Users, pk=request.user.pk)
    if request.method == 'POST':
        form = UsersProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipebook:profile')
        else:
            return render(request, 'recipebook/profile.html', {'form': form})
    else:
        form = UsersProfileForm(instance=request.user)
    return render(request, 'recipebook/profile.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UsersAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipebook:home')
    else:
        form = UsersAuthenticationForm()
    return render(request, 'recipebook/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('recipebook:home')
