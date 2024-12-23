# Recipe App

## Overview

The Recipe App is a web application built using Python and the Django Framework. It is a dynamic, multi-user application, letting users sign up and create their own content. Users can create, read, modify recipes and search for recipes based on ingredients. There is also an admin panel for data handling and visualization.

## User Goals
Users can:
- Create and modify recipes containing ingredients, cooking time and a difficulty parameter automatically calculated by the application.
- Search for recipes by ingredients.

## Key Features
- Allows for user authentication, login and logout
- Lets users search for recipes according to ingredients
- App automatically rates each recipe by difficulty level
- Receives user input and handle errors appropriately
- Displays more details on each recipe if the user requests it
- Adds user recipes to an SQLite database
- Includes a Django Admin dashboard for working with database entries
- Shows statistics and visualizations based on trends and data analysis.

## Technical Requirements
- Python 3.6+ and Django 3 compatibility.
- Exception handling with user-friendly error messages.
- PostgreSQL for production and SQLite for development database connectivity.
- Easy-to-use interface with simple input forms and easy to follow instructions.
- Code documentation and automated tests hosted on GitHub (includes "requirements.txt" for easy project setup).