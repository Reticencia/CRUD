from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField()
    fecha_vencimiento=models.DateField()
    completa=models.BooleanField(default=False)