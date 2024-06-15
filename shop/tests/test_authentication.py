from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        
    def test_login_required_redirect(self):
        response = self.client.get(reverse('shop:car_add'))
        self.assertRedirects(response,
                             f'{reverse("users:login")}?next={reverse("shop:car_add")}')
        
    def test_login_sucessful(self):
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)
        response = self.client.get(reverse('shop:car_add'))
        self.assertEqual(response.status_code,200)