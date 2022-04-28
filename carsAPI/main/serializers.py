from rest_framework import serializers
from .models import CarModel, CarBrand, UserCar


class CarModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'car_brand', 'created_at', 'updated_at','deleted_at']


class CarBrandSerializer(serializers.ModelSerializer):
    car_models = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'car_models', 'created_at', 'deleted_at']


class UserCarSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)
    car = serializers.SerializerMethodField(read_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserCar
        fields = ['id','car', 'username','first_reg', 'odometer', "car_brand",
                  "car_model",'created_at', 'deleted_at']

    def get_car(self, obj):
        return str(obj)
