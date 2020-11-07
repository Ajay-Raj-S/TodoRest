from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoTable
from .serializers import TodoSerializer


class TodoList(APIView):
    def get(self, request, format=None):
        todo = TodoTable.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoManage(APIView):

    def get_object(self, pk):
        try:
            return TodoTable.objects.get(pk=pk)
        except TodoTable.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        breakpoint()
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        data = JSONParser().parse(request)
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo != None:
            todo.delete()
        
        return Response(status=204)
