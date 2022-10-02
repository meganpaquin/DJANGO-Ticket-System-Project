from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Ticket(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status_choices = models.TextChoices('status', 'Open Complete Archived')
    status = models.CharField(default="Open", choices=status_choices.choices, max_length=10)

    #change the admin page list view to show the title
    def __str__(self):
        return self.title


    #what to do when the new data is finished adding, return to list view
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])