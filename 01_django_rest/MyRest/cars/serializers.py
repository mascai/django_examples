from rest_framework import serializers
from cars.models import Cars


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'vin', 'user')


class CarDetailsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # hide user field
    class Meta:
        model = Cars
        fields = '__all__' # serialize all fields
