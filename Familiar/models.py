from django.db import models

class Familiar (models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Edad = models.IntegerField()
    Esta_vivo = models.BooleanField()

