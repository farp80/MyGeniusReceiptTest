from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Recipes, Users
from rest_framework.exceptions import ValidationError
from api.serializers import RecipesSerializer

def error_object(msg, data=None):
    return {
        "details": msg
    }

class UsersView(APIView):
    def get(self,request,user_id=None):
        if user_id is not None:
            user = Users.objects.get(id = user_id)
            recipes = user.user_recipe.all()
            serializer = RecipesSerializer(recipes, many=True)
            return Response(serializer.data)
        else:
           return Response(status=status.HTTP_200_OK)

class RecipesView(APIView):
    def get(self,request,recipe_id=None):
        if recipe_id is not None:
            recipe = Recipes.objects.get(id = recipe_id)
            serializer = RecipesSerializer(recipe, many=False)
            return Response(serializer.data)
        else:
            allRecipes = Recipes.objects.all()
            serializer = RecipesSerializer(allRecipes, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = RecipesSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,recipe_id):
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,recipe_id):         
        try:
            recipe = Recipes.objects.get(id=recipe_id)
            serializer = RecipesSerializer(recipe, data = request.data)
        except Recipes.DoesNotExist:
            return Response(error_object('Not found.'), status=status.HTTP_404_NOT_FOUND)        
       
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


