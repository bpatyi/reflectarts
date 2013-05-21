from django.views.generic import View, ListView, DetailView
from django.template.response import TemplateResponse, HttpResponse

from newsletter.models import NewsLetter

class NewsLetterList(ListView):
    context_object_name = "newsletter_list"
    template_name = "newsletter_list.html"
    paginate_by = 10

    def get_queryset(self):
        return NewsLetter.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NewsLetterList, self).get_context_data(**kwargs)
        return context
