from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'username', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff', False)
        is_superuser = validated_data.pop('is_superuser', False)
        user = User.objects.create_user(
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
            company=validated_data.get('company',''),
            position=validated_data.get('position',''),
        )
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")
        return {'user': user}