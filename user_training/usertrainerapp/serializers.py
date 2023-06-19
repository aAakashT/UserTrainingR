from rest_framework import serializers
from usertrainerapp.models import  User, TrainingModule, Review, Otp
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        # extra_kwargs = {'password': {'write_only': True}}
        
        # print(group)
        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            group = Group.objects.filter(name='User')
            print(group)
            try:
                user = User.objects.get(email = email)   
                return "email already registered kindly SignIn"
            except User.DoesNotExist():
                user = User.objects.create(username = username, email = email)
                user.set_password(password)
                user.groups.add(group[0])
                user.save()   
                # return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password')


class TrainingmoduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = '__all__'
        
class TrainingAssignmentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()        
    training_module_id = serializers.IntegerField()        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'team_leader', )

