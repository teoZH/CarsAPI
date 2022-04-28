from rest_framework import routers
from .views import CarBrandViewSet, CarModelViewSet, UserCarViewSet

router = routers.DefaultRouter()
router.register('brands', CarBrandViewSet, basename='brands')
router.register('models', CarModelViewSet, basename='models')
router.register('cars', UserCarViewSet, basename='cars')

urlpatterns = router.urls
