from django.urls import path

from kitchen.views import (
    HomePageView, DishTypeListView, CookListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "kitchen"
