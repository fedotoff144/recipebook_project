from django.contrib import admin
from recipebook.models import Users, RecipeCategory, Recipe

# Register your models here.
admin.site.register(Users)
admin.site.register(RecipeCategory)
admin.site.register(Recipe)
