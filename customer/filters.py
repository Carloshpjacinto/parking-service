from dj_rql.filter_cls import AutoRQLFilterClass

from customer.models import Customer


class CustomerFilterClass(AutoRQLFilterClass):
    MODEL = Customer
