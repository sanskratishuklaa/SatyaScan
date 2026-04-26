from django.urls import path
from .views import ScanProfileView, ScanHistoryView

urlpatterns = [
    path('scan/', ScanProfileView.as_view()),
    path('history/', ScanHistoryView.as_view()),
]