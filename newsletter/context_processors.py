from newsletter.models import NewsLetter

def newsletter_processor(request):
    newsletter = NewsLetter.objects.all().order_by('-date')
    return { 'newsletter': newsletter[:10] }
