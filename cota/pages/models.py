from django.db import models
from django.utils.timezone import now


# Create your models here.
class Page(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo')
    contenido = models.TextField(verbose_name='Contenido de la página')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name='Página'
        verbose_name_plural = 'Páginas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo