from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, )
    groups = models.ManyToManyField(Group, blank=True, related_name = 'users', default='User')
    team_leader = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class TrainingModule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class AssignmentTraining(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_module = models.ForeignKey(TrainingModule, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True) 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given')
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)                

class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)