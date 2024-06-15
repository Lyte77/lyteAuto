from django.test import TestCase
from django.urls import reverse
from shop.models import Car,Manufacturer,Category

class CarListViewTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name='Toyota')
        self.category = Category.objects.create(name='Sedan')
        self.car = Car.objects.create(
            name='Camry',
            manufacturer = self.manufacturer,
            category = self.category,
            price = 3000,
            description = 'A reliable Sedan',


        )

    def test_car_list_view(self):
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Camry')