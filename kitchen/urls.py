from django.urls import path

from kitchen.views import (
    HomePageView,
    DishTypeListView,
    CookListView,
    DishListView,
    CookDetailView,
    DishDetailView,
    DishTypeDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView, CookCreateView, CookDeleteView, CookUpdateView, DishDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]

app_name = "kitchen"
