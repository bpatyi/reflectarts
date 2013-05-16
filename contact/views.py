from django.views.generic import View
from django.template.response import TemplateResponse, HttpResponse

from contact.models import Contact
from contact.forms import ContactForm
from utils.tools import getIntro


class Contact(View):
    template = 'contact.html'
    http_method_names = ['get', 'post']
    form = ContactForm
    intro = getIntro(5)

    def get(self, request, *args, **kwargs):
        contact_information = None

        form = self.form()

        context = {
            'contact_information': contact_information,
            'contact_form': form,
            'intro': self.intro,
        }

        return TemplateResponse(request, self.template, context)

    def post(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, self.template, context)
