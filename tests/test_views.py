from django.test import TestCase
from Restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.serializers import MenuItemSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=200, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=150, inventory=30)

    def test_get_all(self):
        url = '/restaurant/menu/'
        response = self.client.get(url)

        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)