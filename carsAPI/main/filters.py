from django_filters import rest_framework as filters
from .models import CarModel, CarBrand, UserCar


class BrandFilter(filters.FilterSet):
    model = filters.CharFilter(field_name='car_models__name', lookup_expr='icontains')

    class Meta:
        model = CarBrand
        fields = {'name': ['icontains', 'iexact']}


class ModelFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="car_brand__name", lookup_expr='icontains')

    class Meta:
        model = CarModel
        fields = {'name': ['icontains', 'iexact']}


class UserCarFilter(filters.FilterSet):
    less_than = filters.DateFilter(field_name='first_reg', lookup_expr='lte')
    greater_than = filters.DateFilter(field_name='first_reg', lookup_expr='gte')
    brand = filters.CharFilter(field_name='car_brand__name', lookup_expr='icontains')
    model = filters.CharFilter(field_name='car_model__name', lookup_expr='icontains')
    username = filters.CharFilter(field_name='user__username', lookup_expr='icontains')

    class Meta:
        model = UserCar
        fields = {
            'odometer': ['exact', 'lt', 'gt'],
        }
