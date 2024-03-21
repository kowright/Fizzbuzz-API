from django.db import models

class Fizzbuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True) 
    useragent = models.CharField(max_length=255) 
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fizzbuzz_id}: {self.message}' 
