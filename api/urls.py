from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('recipes/<int:recipe_id>', views.RecipesView.as_view(), name='recipe-id'),
    path('user/<int:user_id>', views.RecipesView.as_view(), name='user-id')
]
