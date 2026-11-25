from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from question_management.serializers import QuestionSerializer
from question_management.models import Question

from assesment_management.models import Assesment

# Create your views here.

class QuestionCreateView(CreateAPIView):
    serializer_class=QuestionSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        assesment_id= self.kwargs.get("pk")
        assesment_object=get_object_or_404(Assesment,id=assesment_id)

        
        return serializer.save(assessment=assesment_object)




class QuestionRetreiveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=QuestionSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Question.objects.all()
