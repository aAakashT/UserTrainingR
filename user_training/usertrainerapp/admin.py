from django.contrib import admin
from .models import User,TrainingModule, AssignmentTraining, Review, Otp
# Register your models here.

admin.site.register([User, TrainingModule, AssignmentTraining, Review, Otp])