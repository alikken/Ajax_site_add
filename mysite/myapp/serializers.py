from rest_framework import serializers
from myapp import models


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cinema
        fields = '__all__'
