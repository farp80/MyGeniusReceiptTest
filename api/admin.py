from django.contrib import admin
from api.models import Users, Recipes, Steps, Ingredients
# Register your models into de django admin here.
admin.site.register(Users)
admin.site.register(Recipes)
admin.site.register(Ingredients)
admin.site.register(Steps)

