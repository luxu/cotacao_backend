from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('moeda.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
