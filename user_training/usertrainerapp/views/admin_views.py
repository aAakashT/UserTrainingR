from django.shortcuts import render
from usertrainerapp.serializers import TrainingmoduleSerializer,AssignmentTrainingSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from usertrainerapp.models import TrainingModule, AssignmentTraining, Review 
from usertrainerapp.permissions import IsAdmin

class TrainingViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdmin,]
    serializer_class = TrainingmoduleSerializer
    queryset = TrainingModule.objects.all()

class AssignmentViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdmin,]
    serializer_class = AssignmentTrainingSerializer
    queryset = AssignmentTraining.objects.all()

class ReviewViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdmin,]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
