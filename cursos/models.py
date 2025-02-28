# cursos/models.py
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    duracion = models.IntegerField()  # Duración en horas
    url_youtube = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre
