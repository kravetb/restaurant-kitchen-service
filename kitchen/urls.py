from django.urls import path

from kitchen.views import (
    HomePageView, DishTypeListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen"
