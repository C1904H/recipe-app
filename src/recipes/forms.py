from django import forms
from .models import Recipe

# SEARCH__CHOICES = [
#   ('name', 'Recipe Name'),
#   ('cooking_time', 'Cooking Time (mins)'),
#   ('difficulty', 'difficulty')
# ]
# CHART__CHOICES = (          
#    ('#1', 'Bar chart'),    
#    ('#2', 'Pie chart'),
#    ('#3', 'Line chart')
# )

class RecipeSearchForm(forms.Form): 
    DIFFICULTY_CHOICES = [
        ('', 'All'),
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard'),
    ]

    name = forms.CharField(
        required=False,
        label="Recipe Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter recipe name'})
    )
    difficulty = forms.ChoiceField(
        required=False,
        choices=DIFFICULTY_CHOICES,
        label="Difficulty",
    )
    ingredient = forms.CharField(
        required=False,
        max_length=120,
        label='Ingredient',
        widget=forms.TextInput(attrs={'placeholder': 'Enter desired ingredient'})
    )

  


