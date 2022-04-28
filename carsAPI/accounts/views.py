from django.contrib.auth import logout
from rest_framework import generics, status
from .models import MainProfile
from .serializers import RegisterMainProfileSerializer,UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import views
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = MainProfile.objects.all()
    serializer_class = RegisterMainProfileSerializer


class LoginView(ObtainAuthToken):
    pass


class LogoutView(views.APIView):
    permissions = [permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        if request.user.auth_token:
            self.request.user.auth_token.delete()
        logout(request)
        return Response({'Message': 'Logout successful'}, status=status.HTTP_200_OK)


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    queryset = MainProfile.objects.all()
    serializer_class = UserSerializer

    #todo-should implement soft delete
    #todo-should implement some login restrictions

