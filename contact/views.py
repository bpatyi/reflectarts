from django.views.generic import View
from django.template.response import TemplateResponse, HttpResponse


class Contact(View):
    template = 'contact.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, self.template, context)

    def post(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, self.template, context)
