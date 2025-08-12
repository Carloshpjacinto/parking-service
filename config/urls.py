from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customer.urls')),
    path('api/v1/', include('parking.urls')),
    path('api/v1/', include('vehicle.urls')),

    path('', admin.site.urls),
]
