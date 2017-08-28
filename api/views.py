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
        meta = request.META
        body = json.loads(request.body)
        
        url = 'https://staging-api.osf.io/v2/nodes/'+body['data']['id']+'/'
        headers = {'Authorization': meta['HTTP_AUTHORIZATION']} 
        r = requests.get(url, headers=headers)
        #ipdb.set_trace()
        

        
        print('!!!!!!!META PRINTED BELOW   !!!!!!!!')
        print(meta['HTTP_AUTHORIZATION'])
        print(body['data']['id'])
        
        if len(r.json()['data']['attributes']['current_user_permissions']) == 1:
            print('NOOOOO PERMS perms ')
            return Response({'ERROR_MESSAGE':'Error: you do not have write access to this project' , 'status': '403'})
            #Response({'Err String':'error yo','Body': request.body, 'json': r.json()['data']['attributes']['current_user_permissions'][1]})
        else:
            print('the user has perms ')
            return super(HomeViewSet, self).create(arg)
        
