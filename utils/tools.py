from intro.models import Intro
from newsletter.models import NewsLetter


def getIntro(subpageId):
    try:
        intro_ = Intro.objects.get(subpage__id=subpageId)
    except Intro.DoesNotExist:
        intro_ = None

    return intro_
