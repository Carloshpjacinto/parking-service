from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from .models import Customer
from .serializers import CustomerSerializer
from .filters import CustomerFilterClass

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]