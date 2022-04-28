from django.urls import path, re_path
from rest_framework import routers
from .views import LoginView, RegisterView, UserViewSet, LogoutView

router = routers.DefaultRouter()

router.register(r'users',UserViewSet,basename='users')


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
] + router.urls


