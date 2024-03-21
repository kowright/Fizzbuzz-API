#describes going from python to JSON
 
from rest_framework import serializers
from .models import Fizzbuzz
class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fizzbuzz
        fields = ['fizzbuzz_id', 'useragent', 'creation_date', 'message']