from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, recipe_search, recipe_analytics

app_name = 'recipes'

urlpatterns = [
  path('', home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('search', recipe_search, name='search'),
  path('analytics', recipe_analytics, name='recipe_analytics'),
]