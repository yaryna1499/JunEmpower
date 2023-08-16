from rest_framework import serializers
from .models import CustomUser, Project, Comment, Like, Specialization, Technology



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 
                  'email', 'date_joined', 'profile_picture', 'is_active']
