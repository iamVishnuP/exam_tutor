from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from assesment_management.models import Assesment
from assesment_management.serializers import AssesmentSerializer
from assesment_management.permissions import IsOwner

from datetime import datetime,timedelta

# Create your views here.

class AssesmentListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]
    def get(self,request):
        qs= Assesment.objects.filter(trainer=request.user)
        serialzer_instance= AssesmentSerializer(qs,many=True)
        return Response(serialzer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=AssesmentSerializer(data=form_data)

        # custom logic
        if serializer_instance.is_valid():
            exam_date=serializer_instance.validated_data['exam_date']

            start_time=serializer_instance.validated_data['start_time']
            
            duration=serializer_instance.validated_data['duration']

            end_date_time=datetime.combine(exam_date,start_time)+timedelta(hours=duration)

            end_time=end_date_time.time()

        

        
            serializer_instance.save(trainer=request.user,end_time=end_time)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class AssesmentRetreiveUpdateDeleteView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk=None):
        qs=get_object_or_404(Assesment,id=pk)
        serializer_instance=AssesmentSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        instance=get_object_or_404(Assesment,id=pk)
        serializer_instance=AssesmentSerializer(data=form_data,instance=instance)

        #custom logic
        if serializer_instance.is_valid():
            start_time=serializer_instance.validated_data.get('start_time',instance.start_time)

            exam_date=serializer_instance.validated_data.get('exam_date',instance.exam_date)

            duration=serializer_instance.validated_data.get('duration',instance.duration)

            end_date_time=datetime.combine(exam_date,start_time)+timedelta(hours=duration)

            end_time=end_date_time.time()
            
        

        

            
        
            serializer_instance.save(end_time=end_time)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        instance=get_object_or_404(Assesment,id=pk)
        instance.delete()
        return Response({"message":"deleted"})
