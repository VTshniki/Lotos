from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

from .models import *


class GPSDataView(APIView):
    def get(self, request):
        data = GPSData.objects.all()
        serial = GPSSerial(data, many=True)
        return Response({'GPDData': serial.data})

    def post(self, request):
        data = request.data.get('gps')
        serial = GPSSerial(data=data)
        if serial.is_valid(raise_exception=True):
            data = serial.save()
        return Response({"success": f'{data.utc_time} saved'})


class PhysicalIndicatorsDataView(APIView):
    def get(self, request):
        data = PhysicalIndicatorsData.objects.all()
        serial = PhysicalIndicatorsDataSerial(data, many=True)
        return Response({'PhysicalIndicatorsData': serial.data})

    def post(self, request):
        data = request.data.get('pid')
        serial = PhysicalIndicatorsDataSerial(data=data)
        if serial.is_valid(raise_exception=True):
            data = serial.save()
        return Response({"success": f'{data.device_name} saved'})


class SystemDataView(APIView):
    def get(self, request):
        data = SystemData.objects.all()
        serial = SystemDataSerial(data, many=True)
        return Response({'SystemData': serial.data})

    def post(self, request):
        data = request.data.get('sys-data')
        serial = SystemDataSerial(data=data)
        if serial.is_valid(raise_exception=True):
            data = serial.save()
        return Response({"success": f'{data.type_process} saved'})


class UsersView(APIView):
    def get(self, request, name, password):
        data = Users.objects.filter(name=name, password=password)
        serial = UsersSerial(data, many=True)
        return Response({'users': serial.data})

    def post(self, request):
        data = request.data.get('users')
        serial = UsersSerial(data=data)
        if serial.is_valid(raise_exception=True):
            data = serial.save()
        return Response({"success": f'{data.name} saved'})