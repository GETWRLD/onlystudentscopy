from .models import Profile
from django.db.models import Q

def searchprofiles(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if search_query != '':
        profiles = Profile.objects.distinct().filter(
            Q(username__icontains=search_query)
        )
        return profiles
