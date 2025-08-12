from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from .models import VehicleType, Vehicle
from .serializers import VehicleTypeSerializer, VehicleSerializer
from config.permissions import IsOwnerOfVehicleOrRecord
from vehicle.filters import VehicleTypeFilterClass, VehicleFilterClass

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
