from django.shortcuts import render
from usertrainerapp.serializers import TrainingmoduleSerializer,ReviewSerializer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from usertrainerapp.models import TrainingModule, Review 
from usertrainerapp.permissions import IsAdmin, IsTeamLead, IsUser

class TrainingViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdminUser, IsAdmin,]
    serializer_class = TrainingmoduleSerializer
    queryset = TrainingModule.objects.all()

class ReviewViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdminUser, IsAdmin,] 
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
