from django.views.generic import View
from django.contrib.flatpages.models import FlatPage
from django.template.response import TemplateResponse, HttpResponse
from utils.tools import getIntro

from artists.models import Artist
from exhibitions.models import Exhibition


class Index(View):
    template = 'index.html'
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        intro = getIntro(1)

        selected_artists = Artist.objects.filter(selected=True).order_by('-created_at')

        exhibitions = Exhibition.objects.all()[:10]

        context = {
            'intro': intro,
            'selected_artists': selected_artists,
            'exhibitions': exhibitions,
        }

        return TemplateResponse(request, self.template, context)


class Services(View):
    template = 'service.html'
    http_method_names = ['get',]

    def get(self, request, *args, **kwargs):
        flatpage = FlatPage.objects.get(title='Services')
        intro = getIntro(4)

        context = {
            'flatpage': flatpage,
            'intro': intro,
        }

        return TemplateResponse(request, self.template, context)
