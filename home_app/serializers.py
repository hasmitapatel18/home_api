from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ("owner_first_name", "owner_last_name", "address_line_1", "postcode")
