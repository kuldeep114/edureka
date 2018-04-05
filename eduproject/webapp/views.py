from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializer, employeeCreateSerializer
from rest_framework import generics


# Create your views here.
class employeeList(APIView):

    def get(self, request):

        employees1 = employees.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)


class employeesCreateAPIViews(generics.CreateAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeCreateSerializer

class employeesDetailAPIViews(generics.RetrieveAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'first_name'


class employeesUpdateAPIViews(generics.UpdateAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'first_name'


class employeesDeleteAPIViews(generics.DestroyAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'first_name'