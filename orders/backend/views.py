from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Shop, Product, Category, Order, OrderItem, Contact
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,

)



# Вход
class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Установить сессию (если вы используете сессии)
        request.session.flush()
        request.session['user_id'] = user.id
        request.session.save()

        return Response({
            'session_key': request.session.session_key,
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }, status=status.HTTP_200_OK)

# Регистрация
class RegistrationAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'id': user.id, 'email': user.email}, status=status.HTTP_201_CREATED)