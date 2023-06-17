from django.contrib import admin
from .models import User,TrainingModule, AssignmentTraining, Reiew
# Register your models here.

admin.site.register([User, TrainingModule, AssignmentTraining, Reiew])