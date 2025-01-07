from django.shortcuts import render
from django.views.generic import ListView, DetailView   
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(ListView, LoginRequiredMixin):
  model = Recipe
  template_name = 'recipes/recipe_list.html'

class RecipeDetailView(DetailView, LoginRequiredMixin):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'