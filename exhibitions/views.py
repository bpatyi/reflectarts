from django.views.generic import View, ListView, DetailView
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

class ExhibitionDetail(DetailView):
    model = Exhibition
    template_name = 'exhibition_detail.html'
    queryset = Exhibition.objects.all()

    def __init__(self, *args, **kwargs):
        super(ArtistDetail, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qs = super(ArtistDetail, self).get_queryset()
        slug = self.kwargs.get('slug', None)

        qs = Exhibition.object.get(slug=slug)

        return qs


    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)

        return context
