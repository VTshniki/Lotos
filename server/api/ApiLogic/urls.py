from django.urls import path
from .views import GPSDataView, PhysicalIndicatorsDataView, SystemDataView

urlpatterns = [
    path('gps/', GPSDataView.as_view(), name='GPSData'),
    path('sys-data/', PhysicalIndicatorsDataView.as_view(), name='PhysicalIndicatorsData'),
    path('pid/', SystemDataView.as_view(), name='SystemData')
]