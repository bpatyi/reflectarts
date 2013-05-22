from django.views.generic import View, ListView, DetailView
from django.template.response import TemplateResponse, HttpResponse
from artists.models import Artist

from utils.tools import getIntro


class ArtistList(ListView):
    context_object_name = "artist_list"
    template_name = "artist_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Artist.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)

        context['intro'] = getIntro(3)
        return context


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    queryset = Artist.objects.all()

    def __init__(self, *args, **kwargs):
        super(ArtistDetail, self).__init__(*args, **kwargs)
        self.intro = None


    def get_queryset(self):
        qs = super(ArtistDetail, self).get_queryset()
        slug = self.kwargs.get('slug', None)

        qs = Artist.objects.filter(slug=slug)

        return qs


    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)

        context['intro'] = getIntro(3)
        return context

