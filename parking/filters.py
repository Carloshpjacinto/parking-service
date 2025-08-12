from dj_rql.filter_cls import AutoRQLFilterClass
from .models import ParkingSpot, ParkingRecord


class ParkingSpotFilterClass(AutoRQLFilterClass):
    MODEL = ParkingSpot

class ParkingRecordFilterClass(AutoRQLFilterClass):
    MODEL = ParkingRecord