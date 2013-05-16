from django.views.generic import View, ListView
from django.template.response import TemplateResponse, HttpResponse
from exhibition.models import Exhibition, ExhibitionDesciptor


class ExhibitionList(ListView):
    context_object_name = "exhibition_list"
    template_name = "exhibition_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Exhibiton.objects.all().order_by('-exhibitiondescriptor__from_date')

    def get_context_data(self, **kwargs):
        context = super(ExhibitionList, self).get_context_data(**kwargs)
        return context
