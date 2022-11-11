from django.shortcuts import render
from .models import Student_details
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework.views import APIView



#Class based view

class Studentdata(APIView):
    def get(self, request, pk=None, format=None):
        
        if pk is not None:
            a=Student_details.objects.get(id=pk)
            serializer=Studentserializer(a)
            return Response(serializer.data)

#--If pk is none the following code for all data will run
        a=Student_details.objects.all()
        serializer=Studentserializer(a, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk=None, format=None):
        serializer= Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The data has saved")
        return Response("Error, Check your data again ")
    
    def put(self,request, pk, format=None):
        a=Student_details.objects.get(id=pk)
        serializer=Studentserializer(a, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Your data has been saved")

    def delete(self, request, pk, format=None):
        a=Student_details.objects.get(id=pk)
        a.delete()
        return Response("Successfully deleted")
