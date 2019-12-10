from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import *
from .serializers import HomeSerializer

# Create your tests here.
# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_home(owner_first_name="", owner_last_name="", address_line_1="", postcode=""):
        if owner_first_name != "" and owner_last_name != "" and address_line_1 != "" and postcode != "":
            Home.objects.create(owner_first_name=owner_first_name, owner_last_name=owner_last_name, address_line_1=address_line_1, postcode=postcode)

    def setUp(self):
        # add test data
        self.create_home("John", "Smith", "3 Northwick Avenue", "HA3 0AA")
        self.create_home("Jane", "Doe", "13 Prestwood Avenue", "HA3 8JZ")
        self.create_home("Lucas", "Dale", "34  Ash Lane", "IP23 6RL")
        self.create_home("Billy", "Ferguson", "101  Chapel Lane", "SW38 0WA")


class GetAllHomesTest(BaseViewTest):

    def test_get_all_homes(self):
        """
        This test ensures that all homes added in the setUp method
        exist when we make a GET request to the homes/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("homes-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Home.objects.all()
        serialized = HomeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
