from rest_framework import serializers
from api.models import Recipes, Users, Steps, Ingredients


class RecipesSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Recipes
        fields = ('id', 'name', 'user')

class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = ('id', 'step_text')

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'text')