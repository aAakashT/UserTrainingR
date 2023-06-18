from rest_framework import serializers
from usertrainerapp.models import  User, TrainingModule, AssignmentTraining, Review, Otp

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            try:
                user = User.objects.get(email = email)   
                return "email already registered kindly SignIn"
            except User.DoesNotExist():
                user = User.objects.create_user(username = username, password = password, email = email)   
                return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password')


class TrainingmoduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = '__all__'    
        
class AssignmentTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTraining
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = '__all__'         