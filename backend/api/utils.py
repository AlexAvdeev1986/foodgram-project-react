from django.shortcuts import get_object_or_404

from recipes.models import Ingredient, IngredientAmount


def ingredient_amount_set(recipe, ingredients_data):
    """Создает связи рецепта с количеством ингредиента."""
    for ingredient_data in ingredients_data:
        id = ingredient_data.get("id")
        ingredient = get_object_or_404(Ingredient, id=id)
        amount = ingredient_data.get("amount")
        IngredientAmount.objects.create(
            recipe=recipe, ingredient=ingredient, amount=amount
        )
