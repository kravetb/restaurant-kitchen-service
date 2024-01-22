from django.views import generic

from kitchen.models import DishType, Cook, Dish


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


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().select_related("dish_type")
