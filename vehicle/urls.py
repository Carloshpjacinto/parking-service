from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VehicleTypeViewSet, VehicleViewSet

router = DefaultRouter()
router.register("vehicle/type", VehicleTypeViewSet)
router.register("vehicle", VehicleViewSet)


urlpatterns = [path("", include(router.urls))]
