from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class GPSDataView(APIView):
    def get(self, request):
        data = GPSData.objects.all()
        return Response({'GPDData': data})


class PhysicalIndicatorsDataView(APIView):
    def get(self, request):
        data = PhysicalIndicatorsData.objects.all()
        return Response({'PhysicalIndicatorsData': data})


class SystemDataView(APIView):
    def get(self, request):
        data = SystemData.objects.all()
        return Response({'SystemData': data})