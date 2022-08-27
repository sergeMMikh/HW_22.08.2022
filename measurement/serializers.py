from rest_framework import serializers

from measurement.models import Sensor, TemperatureMeasurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['temperature', 'date']
