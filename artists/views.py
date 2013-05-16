from django.views.generic import View, ListView, DetailView
from django.template.response import TemplateResponse, HttpResponse
from artists.models import Artist

class ArtistList(ListView):
    context_object_name = "artist_list"
    template_name = "artist_list.html"

    def get_queryset(self):
        return Artist.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        return context


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_list.html'
    queryset = Artist.objects.all()

    def __init__(self, *args, **kwargs):
        super(ArtistDetail, self).__init__(*args, **kwargs)


    def get_queryset(self):
        qs = super(ArtistDetail, self).get_queryset()

        return qs


    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)

        return context

