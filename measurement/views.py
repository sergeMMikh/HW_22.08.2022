from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

from .models import Sensor, Measurement


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(name=request.POST.get('name'),
                              description=request.POST.get('description'))
        return Response({'status': 'Ok'})


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        detector_id = Sensor.objects.get(id=request.POST.get('detector_id'))
        Measurement.objects.create(detector_id=detector_id,
                                   temperature=request.POST.get('temperature'))
        return Response({'status': 'Ok'})
