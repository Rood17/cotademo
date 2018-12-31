from django.db import models
from django.utils.timezone import now


# Create your models here.
class About(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    puesto = models.CharField(max_length=200, verbose_name='Puesto', null=True)
    descripcion = models.TextField(verbose_name='Escribe aquí una breve descripción del libro')
    imagen = models.ImageField(verbose_name="Fotografía", upload_to='about')
    link = models.URLField(verbose_name='Link red social', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name='Equipo'
        verbose_name_plural = 'Equipo'
        ordering = ['created']

    def __str__(self):
        return self.nombre