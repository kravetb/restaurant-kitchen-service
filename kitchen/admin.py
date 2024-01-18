from django.contrib import admin

from kitchen.models import Cook, DishType, Dish


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ["year_of_experience", ]
    fieldsets = (("Additional info", {"fields": ("year_of_experience",)}), )
    ordering = ["-years_of_experience", ]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ["dish_type", ]
    search_fields = ["name", ]


admin.site.register(DishType)
