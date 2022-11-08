from django.conf import settings
from django.db import models
from django.utils import timezone


class Usuario(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre + " " + self.apellido