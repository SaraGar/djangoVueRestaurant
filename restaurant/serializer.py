from rest_framework import serializers
from .models import  Menu, MenuItem, Location

class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
class LocationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
