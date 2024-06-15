from django.test import TestCase
from shop.models import Car,Manufacturer,Category

class CarModelTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name='Toyota')
        self.category = Category.objects.create(name='Sedan')
        self.car = Car.objects.create(
            name='Camry',
            manufacturer = self.manufacturer,
            category=self.category,
            price= 3000,
            description='A reliable sedan',
            
        )
    
    def test_car_creation(self):
        self.assertEqual(self.car.name, 'Camry')
        self.assertEqual(self.car.manufacturer.name, 'Toyota')
        self.assertEqual(self.car.category.name, 'Sedan')
        self.assertEqual(self.car.price, 3000)
        self.assertEqual(self.car.description, 'A reliable sedan')
       