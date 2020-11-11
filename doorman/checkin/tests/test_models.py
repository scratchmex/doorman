import pytest
from django.test import TestCase
from pytest_django.asserts import assertContains  # pylint: disable=no-name-in-module

from . import factories
from .. import models


# Create your tests here.
class TestOwnerModel:
    def test_house_rel(self, db):
        owner = factories.OwnerFactory()
        house = factories.HouseFactory(owner=owner)

        assert models.House.objects.filter(owner=owner).exists()

    def test_multiple_factories(self, db):
        owner1 = factories.OwnerFactory()
        print(owner1.user)
        owner2 = factories.OwnerFactory()

        assert owner1 != owner2


class TestVisitorModel:
    def test_multiple_factories(self, db):
        visitor1 = factories.VisitorFactory()
        visitor2 = factories.VisitorFactory()

        assert visitor1 != visitor2


class TestAddressModel:
    def test_multiple_factories(self, db):
        address1 = factories.AddressFactory()
        address2 = factories.AddressFactory()

        assert address1 != address2


class TestHouseModel:
    def test_multiple_factories(self, db):
        house1 = factories.HouseFactory()
        house2 = factories.HouseFactory()

        assert house1 != house2


class TestPlateModel:
    def test_multiple_factories(self, db):
        plate1 = factories.PlateFactory()
        plate2 = factories.PlateFactory()

        assert plate1 != plate2


class TestCheckinModel:
    def test_multiple_factories(self, db):
        checkin1 = factories.CheckinFactory()
        checkin2 = factories.CheckinFactory()

        assert checkin1 != checkin2

    def test_nulls(self, db):
        try:
            checkin = factories.CheckinFactory(visitor=None, time_verified=None,)
        except Exception as e:
            raise

    def test_checkin_rel(self, db):
        house = factories.HouseFactory()
        visitor = factories.VisitorFactory()
        checkin = factories.CheckinFactory(house=house, visitor=visitor,)

        assert house.checkin_set.filter(visitor=visitor).exists()
