from django.urls import path
from .views import GPSDataView, PhysicalIndicatorsDataView, SystemDataView, UsersView

urlpatterns = [
    path('gps/', GPSDataView.as_view(), name='GPSData'),
    path('pid/', PhysicalIndicatorsDataView.as_view(), name='PhysicalIndicatorsData'),
    path('sys-data/', SystemDataView.as_view(), name='SystemData'),
    path('users/<str:name>/<str:password>', UsersView.as_view(), name='users')
]