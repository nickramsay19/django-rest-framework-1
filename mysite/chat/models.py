from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length = 300)
    user = models.CharField(max_length = 300)

    def __str__(self):
        return self.text
