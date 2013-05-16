from newsletter.models import NewsLetter

def newsletter_processor(request):
    try:
        newsletter_ = NewsLetter.objects.all().order_by('date')
    except NewsLetter.DoesNotExist:
        newsletter_ = None

    if len(newsletter_) > 10:
        return { 'newsletter': newsletter_[:10] }
    else:
        return { 'newsletter': newsletter_ }
