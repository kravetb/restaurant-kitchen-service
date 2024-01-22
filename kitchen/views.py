from django.views import generic

from kitchen.models import DishType, Cook


class HomePageView(generic.base.TemplateView):
    template_name = "kitchen/index.html"


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
