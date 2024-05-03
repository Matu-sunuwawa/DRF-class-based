from django.shortcuts import render
from django.http import HttpResponse

from .models import NoteApp
from .serializers import NoteSerializers

from django.http import Http404 
  
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 

# Create your views here.

class ApiOverview(APIView):
    
    def get(self, request):
        api_urls = {
            'Intro Page':'/lists/',
            'Detail View Page':'/detail_list/<str:pk>/',
            'Creating New List':'/create_list/',
            'Updating Specific List':'/update_list/<str:pk>/',
            'Deleting Specific List':'/delete_list/<str:pk>/',
            'Goto':'Another level man using rest cool men',
		}
        return Response(api_urls)
    

class ApiTaskList(APIView):
    def get(self, request, format=None):
        task = NoteApp.objects.all()
        serializer = NoteSerializers(task, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ApiTaskDetail(APIView):
    def get_object(self, pk):
        try:
            return NoteApp.objects.get(id=pk)
        except NoteApp.DoesNotExist:
            raise Http404
        
    def get(self, request,pk, format=None):
        task = self.get_object(pk)
        serializer = NoteSerializers(task)
        return Response(serializer.data)
    
    def put(self, request,pk, format=None):
        task = self.get_object(pk)
        serializer = NoteSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk, format=None):
        task = self.get_object(pk)
        serializer = NoteSerializers(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)