from django.db import models

class Usernames(models.Model):
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    
    role_choices = models.TextChoices('roles', 'Customer Agent Manager')
    role = models.CharField(default="Customer", choices=role_choices.choices, max_length=15)
