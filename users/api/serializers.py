from dataclasses import fields
from rest_framework import serializers
from users.models import User,Freelancer,Client
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_client']

class FreelanceSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)