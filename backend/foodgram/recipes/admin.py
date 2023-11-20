from django.contrib import admin

from .models import (
    Favorite,
    Ingredient,
    IngredientAmount,
    Recipe,
    ShoppingCart,
    Tag,
)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "measurement_unit")
    search_fields = ("name",)
    list_filter = ("name",)


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ("amount", "recipe", "ingredient")
    search_fields = ("recipe__name", "ingredient__name")


class IngredientInline(admin.TabularInline):
    model = IngredientAmount
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "in_Favorite_count")
    search_fields = ("name", "author__username", "tags__name")
    list_filter = ("name", "author__username", "tags__name")
    readonly_fields = ("in_Favorite_count",)
    inlines = (IngredientInline,)

    def in_Favorite_count(self, recipe):
        """Подсчитывает сколько раз рецепт добавлен в избранное."""
        return recipe.Favorite.count()

    in_Favorite_count.short_description = "В избранном"


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "slug")


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("pk", "recipe", "user")
    search_fields = ("user__username", "recipe__name")
    list_filter = ("user__username", "recipe__name")


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ("pk", "recipe", "user")
    search_fields = ("user__username", "recipe__name")
    list_filter = ("user__username", "recipe__name")


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
