from django.urls import path
from measurement.views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='smart_home'),
    path('sensors/<pk>/', SensorView.as_view()),

    path('measurements/', MeasurementView.as_view()),
]
