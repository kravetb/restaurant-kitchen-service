from django.urls import path

from kitchen.views import HomePageView

urlpatterns = [
    path("home/", HomePageView.as_view(), name="index"),
]

app_name = "kitchen"
