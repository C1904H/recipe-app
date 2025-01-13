from django.shortcuts import render
from django.views.generic import ListView, DetailView   
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
from .utils import generate_charts
import pandas as pd

def home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'

@login_required
def recipe_search(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()

    # Filter recipes based on search criteria
    if form.is_valid():
        name = form.cleaned_data.get('name', '')
        difficulty = form.cleaned_data.get('difficulty', '')
        ingredient = form.cleaned_data.get('ingredient', '')

        if name:
            recipes = recipes.filter(name__icontains=name)
        if difficulty:
            recipes = recipes.filter(difficulty=difficulty)
        if ingredient:
            recipes = recipes.filter(ingredients__icontains=ingredient)
        

    # Convert QuerySet to pandas DataFrame
    recipe_df = pd.DataFrame.from_records(
       recipes.values('id', 'name', 'difficulty', 'cooking_time'))

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipes': recipes,
    }
    return render(request, 'recipes/recipe_search.html', context)

@login_required
def recipe_analytics(request):
    # Fetch recipes from the database
    recipes = Recipe.objects.all()

    # Extract data
    recipe_names = [recipe.name for recipe in recipes]
    cooking_times = [recipe.cooking_time for recipe in recipes]
    difficulties = [recipe.difficulty for recipe in recipes]
    ingredient_counts = [len(recipe.ingredients.split(',')) for recipe in recipes]  

    # Create a dictionary for difficulties
    difficulty_counts = {difficulty: difficulties.count(difficulty) for difficulty in set(difficulties)}

    # Generate charts
    charts = generate_charts(recipe_names, cooking_times, difficulty_counts, ingredient_counts)

    return render(request, 'recipes/recipe_analytics.html', {'charts': charts})

