from django.views import generic

from kitchen.models import DishType, Cook, Dish


class HomePageView(generic.base.TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        num_cooks = Cook.objects.count()
        num_dishes = Dish.objects.count()
        num_dish_types = DishType.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_cooks"] = num_cooks
        context["num_dishes"] = num_dishes
        context["num_dish_types"] = num_dish_types
        context["num_visits"] = num_visits
        return context


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
