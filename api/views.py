from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import HomeSerializer
from .models import Home
from rest_framework.response import Response
import requests
import ipdb
import json 


# Create your views here.

class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def create(self, request, *args, **kwargs):
        r = requests.get('https://staging-api.osf.io/v2/nodes/xyp8r/')
        #ipdb.set_trace()
        meta = request.META
        body = json.loads(request.body)
        print('!!!!!!!META PRINTED BELOW   !!!!!!!!')
        print(meta['HTTP_AUTHORIZATION'])
        print(body)
        return Response({'Err String':'error yo','Body': request.body, 'json': r.json()})
        
        #return super(HomeViewSet, self).create(arg)
        
