from rest_framework import serializers
from .models import MainProfile
from django.contrib.auth.password_validation import validate_password


class RegisterMainProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = MainProfile
        fields = ['username', 'password', 'password2', 'email']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'error': 'Password fields do not match!'})
        return attrs

    def create(self, validated_data):
        user = MainProfile.objects.create_user(username=validated_data['username'],
                                               email=validated_data['email'],
                                               password=validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    user_cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = MainProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'favourite_brand', 'email', 'image', 'user_cars']

    def create(self, validated_data):
        raise serializers.ValidationError('error : Not allowed')
