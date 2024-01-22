from django.views import generic

from kitchen.models import DishType


class HomePageView(generic.base.TemplateView):
    template_name = "kitchen/index.html"

