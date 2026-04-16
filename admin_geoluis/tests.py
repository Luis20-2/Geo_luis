from django.contrib.auth.models import User
from django.test import TestCase


class AdminGeoLuisTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester_login', password='secreto123')

    def test_home_page_exposes_jwt_login_section(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'jwtLoginBtn')
        self.assertContains(response, 'loginStatus')

    def test_home_page_hides_main_panel_until_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'playground · respuesta en vivo')

    def test_mobile_login_returns_jwt_tokens(self):
        response = self.client.post('/api/jwt/login/', {
            'username': 'tester_login',
            'password': 'secreto123',
        }, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('access', payload)
        self.assertIn('refresh', payload)
