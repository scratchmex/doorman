from django.test import Client
from pytest_django.asserts import assertContains  # pylint: disable=no-name-in-module

from . import factories
from .. import models


# Create your tests here.
class TestUserModel:
    def test_create(self, db):
        user = factories.UserFactory()

        assert models.User.objects.filter(username=user.username).exists()

    def test_multiple_factories(self, db):
        user1 = factories.UserFactory()
        user2 = factories.UserFactory()

        assert user1 != user2
