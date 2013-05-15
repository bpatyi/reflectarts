from django.views.generic.edit import FormView, View
from django.template.response import TemplateResponse, HttpResponse


class Index(View):
    template = 'base.html'
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, self.template, context)
