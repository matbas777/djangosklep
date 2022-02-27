from . models import Marka

def element_statyczny(request):
    return {'marka': Marka.objects.all(), 'request': request}
