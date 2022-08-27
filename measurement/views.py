# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

from .models import Sensor, Measurement


# @api_view(['GET', 'POST'])
# def sensors_list(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         ser_sens = SensorSerializer(sensors, many=True)
#         data = {'message': 'Hellow'}
#         return Response(ser_sens.data)
#     if request.method == 'POST':
#         return Response({'status': 'Ok'})

# class SensorsView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser_sens = SensorSerializer(sensors, many=True)
#         data = {'message': 'Hellow'}
#         return Response(ser_sens.data)
#
#     def post(self, request):
#         return Response({'status': 'Ok'})

class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'status': 'Ok'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
