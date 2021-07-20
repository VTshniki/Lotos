from django.db import models


class GPSData(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    utc_time = models.IntegerField(verbose_name='время в формате utc')
    date = models.DateField(verbose_name='дата получения gps', auto_now=True)
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

    def __str__(self):
        return 'Это дата о геопозиции девайса время - {}'.format(self.utc_time)


class PhysicalIndicatorsData(models.Model):
    id_connect_device = models.IntegerField(verbose_name='id', primary_key=True)
    data_connect = models.DateTimeField(verbose_name='дата подключения устройства', auto_now=True)
    device_name = models.CharField(max_length=255, verbose_name='имя устройства')
    device_data = models.JSONField(verbose_name='данные с устройства')
    status = models.CharField(max_length=2, verbose_name='статус устройства')

    def __str__(self):
        return 'Это Индикаторы девайса имени - {}'.format(self.device_name)


class SystemData(models.Model):
    system_id = models.IntegerField(verbose_name='id', primary_key=True)
    date = models.DateTimeField(verbose_name='дата получения', auto_now=True)
    type_process = models.CharField(verbose_name='тип процесса', max_length=20)
    utilization_res = models.IntegerField(verbose_name='используемые ресурсы')
    status = models.CharField(max_length=255, verbose_name='статус')
    action = models.CharField(max_length=255, verbose_name='действие системы')

    def __str__(self):
        return 'Это дата системы номера - {}'.format(self.system_id)


class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    permission = models.CharField(default='user', max_length=255)

    def __str__(self):
        return self.name
