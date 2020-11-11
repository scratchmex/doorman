import factory
import string
import random

from .. import models
from ...users.tests.factories import UserFactory


class OwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Owner

    user = factory.SubFactory(UserFactory)


class VisitorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Visitor

    user = factory.SubFactory(UserFactory)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Address

    ext_number = factory.Faker("building_number")
    street = factory.Faker("street_name")
    int_number = factory.Faker("building_number")
    suburb = factory.Iterator(["Centro", "Dos rios", "San Javier"])
    postal_code = factory.Faker("postcode")
    city = factory.Faker("city")
    state = factory.Iterator(["Guanajuato", "Quintana Roo", "Jalisco"])
    country = factory.Faker("country")


class HouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.House

    owner = factory.SubFactory(OwnerFactory)
    address = factory.SubFactory(AddressFactory)


def random_plate():
    alphanumeric = string.ascii_uppercase + string.digits
    choices = random.choices(alphanumeric, k=3)

    return "-".join(choices)


class PlateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Plate

    visitor = factory.SubFactory(VisitorFactory)
    number = factory.LazyFunction(random_plate)


class CheckinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Checkin

    house = factory.SubFactory(HouseFactory)
    visitor = factory.SubFactory(VisitorFactory)
