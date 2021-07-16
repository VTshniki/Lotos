from django.urls import path
from .views import GPSDataView, PhysicalIndicatorsDataView, SystemDataView

urlpatterns = [
    path('gps/', GPSDataView.as_view(), name='GPSData'),
    path('pid/', PhysicalIndicatorsDataView.as_view(), name='PhysicalIndicatorsData'),
    path('sys-data/', SystemDataView.as_view(), name='SystemData')
]