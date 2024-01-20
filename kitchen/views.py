from django.views import generic


class HomePageView(generic.base.TemplateView):
    template_name = "kitchen/index.html"
