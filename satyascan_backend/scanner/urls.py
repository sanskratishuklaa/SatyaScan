from django.urls import path
from .views import ScanProfileView

urlpatterns = [
    path('scan/', ScanProfileView.as_view()),
]