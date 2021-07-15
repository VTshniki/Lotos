from django.db import models


class GPSData(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    utc_time = models.IntegerField(verbose_name='время в формате utc')
    date = models.DateField(verbose_name='дата получения gps')
    latitude = models.FloatField(verbose_name='широта')
    latitude_pw = models.CharField(max_length=2, verbose_name='сторона света')
    longitude = models.FloatField(verbose_name='долгота')
    longitude_pw = models.CharField(max_length=2, verbose_name='сторона света')
    stand_alone_solution = models.IntegerField(verbose_name='тип решения 1-8')
    num_satel_use = models.CharField(max_length=2, verbose_name='кол-во используемых спутников')
    hdop = models.FloatField(verbose_name='геометрический фактор')
    height = models.FloatField(verbose_name='высота над уровнем моря в метрах')
    WSG84 = models.FloatField(verbose_name='высота геоида над эллипсоидом')
    last_dgps = models.IntegerField(verbose_name='', default=0)
    id_dgps = models.IntegerField(verbose_name='', default=0)

