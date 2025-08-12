from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("authentication/api/v1/", include("authentication.urls")),
    path("customer/api/v1/", include("customer.urls")),
    path("parking/api/v1/", include("parking.urls")),
    path("vehicle/api/v1/", include("vehicle.urls")),
    path("", admin.site.urls),
]
