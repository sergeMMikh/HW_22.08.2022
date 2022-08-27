from django.urls import path
from measurement.views import smart_home

urlpatterns = [
    path('demo/', smart_home, name='smart_home'),
]
