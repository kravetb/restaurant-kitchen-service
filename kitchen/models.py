from django.db import models
from django.contrib.auth.models import AbstractUser

from restaurant_kitchen_service.settings import AUTH_USER_MODEL


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)


class Cook(AbstractUser):
    years_of_experience = models.CharField(max_length=63, blank=True)


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2, blank=False)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="cooks"
    )
    cooks = models.ManyToManyField(AUTH_USER_MODEL)
