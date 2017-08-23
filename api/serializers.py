from .models import Home
from rest_framework import serializers


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('guid', 'page_data', 'unpublished_page_data')