from django.test import Client
from pytest_django.asserts import assertContains  # pylint: disable=no-name-in-module

# Create your tests here.
class TestViews:
    def test_index_200(self, client: Client):
        res = client.get("/")
        assertContains(res, "Doorman")
