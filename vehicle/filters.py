from dj_rql.filter_cls import AutoRQLFilterClass

from vehicle.models import VehicleType, Vehicle

class VehicleTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType

class VehicleFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle