from django.shortcuts import render, redirect
from usertrainerapp.serializers import UserSerializer,TrainingAssignmentSerializer, TrainingmoduleSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from usertrainerapp.models import TrainingModule, Review , User
from usertrainerapp.permissions import IsTeamLead
from rest_framework.decorators import api_view, permission_classes 
from usertrainerapp.forms import AssignModuleForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
@api_view(['GET'])
@permission_classes([IsTeamLead])
def get_users(request):
    if request.method == 'GET':
        user = request.user
        users = User.objects.filter(team_leader = user).prefetch_related('modules')
        serializer = UserSerializer(users, many=True)
        return render(request, 'render_users.html', {'users': serializer.data})
    
    if request.method == 'PUT':
        pass

@api_view(['GET'])
@permission_classes([IsTeamLead])
def get_modules(request):
    if request.method == 'GET':
        user = request.user
        t_modules = TrainingModule.objects.all()
        serializer = TrainingmoduleSerializer(t_modules, many=True)
        return render(request, 'user_review.html', {'modules': serializer.data})

# @api_view(['POST','GET' ])
# @permission_classes([IsTeamLead])
# def assign_modules(request):
#     if request.method == 'GET':
#         form = AssignModuleForm()
#         return render(request, 'user_review.html', {'form': form})
#     if request.method == 'POST':
#         form = AssignModuleForm(request.POST)
#         if form.is_valid():
#             form.assign_training()
#         return redirect('user_review.html')    


# @api_view(['POST', 'GET'])
# @permission_classes([IsTeamLead])
# def assign_module

class AssignModules(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)
        training_modules = TrainingModule.objects.all()
        serializer = TrainingmoduleSerializer(training_modules, many=True)
        context = {'user': user,'training_modules': serializer.data}
        return Response(context)

    def post(self, request, user_id):
        serializer = TrainingAssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user_id = serializer.validated_data['user_id']
        training_module_id = serializer.validated_data['training_module_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        try:
            training_module =  TrainingModule.objects.get(id = training_module_id)
        except TrainingModule.DoesNotExist:
            return Response({'error': 'Training not found'}, status=404)
        user.training_module.add(training_module) 
        user.save()
        return Response({'sucess': 'Training module assigned'})  