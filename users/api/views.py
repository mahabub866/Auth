from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import permissions
from users.api.permission import IsClientUser,IsFreelanceUser
from users.api.serializers import ClientSignupSerializer, FreelanceSignupSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions



class http_response(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        return  Response({
            "message":"Account Created Succesfully."
        })

class FreelanceSignupView(generics.GenericAPIView):
    serializer_class=FreelanceSignupSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return  Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"Account Created Succesfully."
        })

    
class ClientSignupView(generics.GenericAPIView):
    serializer_class=ClientSignupSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return  Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"Account Created Succesfully."
        })

class CustomeAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_client':user.is_client,
            'is_freelancer':user.is_freelancer
        })

class LogoutView(APIView):
    def post(self,request,format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class ClientOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated & IsClientUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user
class FreelanceOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated & IsFreelanceUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user