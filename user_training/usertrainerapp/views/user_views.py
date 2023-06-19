from django.shortcuts import render
from usertrainerapp.serializers import TrainingmoduleSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from usertrainerapp.models import TrainingModule, Review 
from usertrainerapp.permissions import IsUser
from rest_framework.views import APIView


@api_view(['GET',])
@permission_classes([IsUser,])
def render_reviews(request):
    user = request.user
    print(user)
    user_reviews = Review.objects.filter(user = user)
    serializer = ReviewSerializer(user_reviews, many=True)
    return render(request, 'user_review.html', {'user_reviews': serializer.data})

@api_view(['GET',])
@permission_classes([IsUser,])
def render_modules(request):
    user = request.user
    print(user)
    user_modules = TrainingModule.objects.filter(user=user)
    serializer = TrainingmoduleSerializer(user_modules, many=True)
    return render(request, 'user_review.html', {'user_reviews': serializer.data})
