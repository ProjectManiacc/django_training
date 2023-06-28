from django.db import models

# Create your models here.
class Employee(models.Model):
    # id = models.AutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=9, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.first_name}\t\t\t\t{self.last_name}\t\t\t\t{self.email_address}'