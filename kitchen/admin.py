from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, DishType, Dish


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ["years_of_experience", ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    ordering = ["-years_of_experience", ]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ["dish_type", ]
    search_fields = ["name", ]


admin.site.register(DishType)
