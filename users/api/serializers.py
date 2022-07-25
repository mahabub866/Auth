from dataclasses import fields
from distutils.log import error
from rest_framework import serializers
from users.models import User,Freelancer,Client
from django.contrib.auth.models import  Group
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','is_client','is_freelancer','is_staff',]


class FreelanceSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{"write_only":True}
        }
    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error":"Password  not match"})
        user.set_password(password)
        user.is_freelancer=True
        user.save()
        Freelancer.objects.create(user=user)
        return user

class ClientSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{"write_only":True}
        }
    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error":"Password  not match"})
        user.set_password(password)
        user.is_client=True
        user.save()
        Client.objects.create(user=user)
        return user