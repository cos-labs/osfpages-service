from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import HomeSerializer
from .models import Home
# Create your views here.

class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def create(self, request, *args, **kwargs):
        return Response('error yo')
        
        #return super(HomeViewSet, self).create(arg)
        
