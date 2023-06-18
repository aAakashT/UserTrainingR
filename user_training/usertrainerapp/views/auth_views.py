from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import generics , permissions
from usertrainerapp.serializers import UserSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class UserRegistration(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class LoginApi(APIView):
    def post(self, request):
        email = request.data.get('email')
        print(email)
        password = request.data.get('password')
        print(password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user:
            login(request, user)
            session_key = request.session.session_key
            request.session.set_expiry(0)
            return Response({'session_key': session_key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutApi(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
