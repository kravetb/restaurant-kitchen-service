from django.urls import path

from kitchen.views import (
    HomePageView, DishTypeListView, CookListView, DishListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "kitchen"
