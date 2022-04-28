from rest_framework import viewsets
from .serializers import CarModelSerializer, CarBrandSerializer, UserCarSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsAdmin
from .models import CarModel, CarBrand, UserCar
from .filters import BrandFilter,ModelFilter


class SoftModelViewSet(viewsets.ModelViewSet):

    def perform_destroy(self, instance):
        instance.soft_delete()


class CarBrandViewSet(SoftModelViewSet):
    serializer_class = CarBrandSerializer
    # For making testing the api easier i commented the 'IsAdmin' part!
    # These permissions do not allow updating or deleting an instance from a basic user
    # User can only make a GET, HEAD, OPTION or POST(create new object)
    permission_classes = [permissions.IsAuthenticated]  # + [IsAdmin]
    queryset = CarBrand.objects.all()
    filterset_class = BrandFilter


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = CarModelSerializer
    # For making testing the api easier i commented this out!
    # These permissions do not allow updating or deleting an instance from a basic user
    # User can only make a GET, HEAD, OPTION or POST(create new object)
    permission_classes = [permissions.IsAuthenticated]  # + [IsAdmin]
    queryset = CarModel.objects.all()
    filterset_class = ModelFilter





class UserCarViewSet(viewsets.ModelViewSet):
    serializer_class = UserCarSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserCar.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.soft_delete()

# Create your views here.
