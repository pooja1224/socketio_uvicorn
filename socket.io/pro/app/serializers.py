from rest_framework import serializers
from . import models

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Details
        fields = '__all__'