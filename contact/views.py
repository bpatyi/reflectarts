from django.views.generic import View
from django.template.response import TemplateResponse, HttpResponse

form contact.models import Contact
from contact.forms import ContactForm

class Contact(View):
    template = 'contact.html'
    http_method_names = ['get', 'post']
    form = ContactForm

    def get(self, request, *args, **kwargs):
        contact_information = Contact.objects.all()[0]

        form = self.form()

        context = {
            'contact_information': contact_information,
            'contact_form': form,
        }

        return TemplateResponse(request, self.template, context)

    def post(self, request, *args, **kwargs):
        context = {}

        return TemplateResponse(request, self.template, context)
