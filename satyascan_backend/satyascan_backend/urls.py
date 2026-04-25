from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 SatyaScan Backend is Running!")

urlpatterns = [
    path('', home),   # 👈 ADD THIS
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/scanner/', include('scanner.urls')),
]
