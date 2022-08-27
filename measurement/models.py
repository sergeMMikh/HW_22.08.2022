from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=526, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class TemperatureMeasurement(models.Model):
    detector_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField(verbose_name='Температура при измерения')
    date = models.DateTimeField(verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение температуры'
        verbose_name_plural = 'Измерения'
