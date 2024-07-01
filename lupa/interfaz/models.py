from django.db import models

# Create your models here.

class Card(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='img_card', blank=True)
    url = models.TextField(blank=True)

    def __str__(self):
        return self.titulo