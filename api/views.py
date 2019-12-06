from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Recipes

class RecipesView(APIView):
    def get(self, request, user_id=None):
        if user_id is not None:
            user = Users.objects.get(id = user_id)
            recipes = user.user_recipe.all()
            serializer = RecipesSerializer(recipes, many=True)
            return Response(serializer.data)
        else:
            allRecipes = Recipes.objects.all()
            serializer = RecipesSerializer(allRecipes, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = RecipesSerializer(data = request.data)

        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, recipe_id):
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)