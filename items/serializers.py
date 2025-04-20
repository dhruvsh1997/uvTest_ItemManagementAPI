# serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Item
        fields = ['itemID', 'itemName', 'day', 'month', 'year']
        # read_only_fields = ['itemID']