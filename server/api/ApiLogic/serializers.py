from rest_framework import serializers as ser
from .models import *


class GPSSerial(ser.Serializer):
    id = ser.IntegerField()
    utc_time = ser.IntegerField()
    date = ser.DateField()
    latitude = ser.FloatField()
    latitude_pw = ser.CharField(max_length=255)
    longitude = ser.FloatField()
    longitude_pw = ser.CharField(max_length=255)
    stand_alone_solution = ser.IntegerField()
    num_satel_use = ser.CharField(max_length=255)
    hdop = ser.FloatField()
    height = ser.FloatField()
    WSG84 = ser.FloatField()
    last_dgps = ser.IntegerField()
    id_dgps = ser.IntegerField()

    def create(self, validated_data):
        return GPSData.objects.create(**validated_data)


class PhysicalIndicatorsDataSerial(ser.Serializer):
    id_connect_device = ser.IntegerField()
    data_connect = ser.DateTimeField()
    device_name = ser.CharField(max_length=255)
    device_data = ser.JSONField()
    status = ser.CharField(max_length=2)

    def create(self, validated_data):
        return PhysicalIndicatorsData.objects.create(**validated_data)


class SystemDataSerial(ser.Serializer):
    system_id = ser.IntegerField()
    date = ser.DateTimeField()
    type_process = ser.CharField(max_length=20)
    utilization_res = ser.IntegerField()
    status = ser.CharField(max_length=255)
    action = ser.CharField(max_length=255)

    def create(self, validated_data):
        return SystemData.objects.create(**validated_data)


class UsersSerial(ser.Serializer):
    name = ser.CharField(max_length=255)
    password = ser.CharField(max_length=255)
    permission = ser.CharField(max_length=255)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)