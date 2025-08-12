from dj_rql.filter_cls import AutoRQLFilterClass

from .models import ParkingRecord, ParkingSpot


class ParkingSpotFilterClass(AutoRQLFilterClass):
    MODEL = ParkingSpot


class ParkingRecordFilterClass(AutoRQLFilterClass):
    MODEL = ParkingRecord
