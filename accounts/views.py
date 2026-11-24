from django.shortcuts import render

from django.shortcuts import render

from accounts.serializers import TutorSerializer,TutorProfileSerializer
from accounts.models import TutorProfile

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

# Create your views here.

class TutorSignUpView(CreateAPIView):

    serializer_class=TutorSerializer


class TutorRetreieveUpdateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        auth_user=request.user
        qs=TutorProfile.objects.get(user=auth_user)
        serializer_instance= TutorProfileSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request):
        auth_user=request.user
        instance=TutorProfile.objects.get(user=auth_user)
        form_data=request.data
        serializer_instance=TutorProfileSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        


