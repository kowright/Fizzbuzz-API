from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Fizzbuzz
from .serializers import FizzBuzzSerializer

class FizzBuzzTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.fizz = Fizzbuzz.objects.create(message='Test message')
        self.fizz = Fizzbuzz.objects.create(message='Message test')
        
    def test_post_fizzbuzz(self):
        data = {"message": "BUZZ"}
        response = self.client.post('http://127.0.0.1:8000/fizzbuzz', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_list_fizzbuzz(self):
        response = self.client.get(f'/fizzbuzz', format='json')
        self.assertEqual(len(response.data), 2)
        
    def test_get_first_fizzbuzz(self):
        response = self.client.get(f'/fizzbuzz/1', format='json')
        self.assertEqual(response.data['message'], 'Test message')