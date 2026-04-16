from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class GeoLuisApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester_api', password='secreto123')

    def test_swagger_endpoint_is_available(self):
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jwt_token_endpoint_returns_tokens(self):
        response = self.client.post('/api/token/', {
            'username': 'tester_api',
            'password': 'secreto123'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_authenticated_user_can_create_employee_with_jwt(self):
        token_response = self.client.post('/api/token/', {
            'username': 'tester_api',
            'password': 'secreto123'
        }, format='json')
        access = token_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        response = self.client.post('/api-luis/empleados/', {
            'nombre_completo': 'Empleado Demo',
            'puesto': 'Backend Developer'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre_completo'], 'Empleado Demo')
