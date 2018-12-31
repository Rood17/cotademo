from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
import json 


# Multiple Choice
from multiselectfield import MultiSelectField

# Serializers
from django.core.serializers.python import Serializer



# Create your models here.
class CategoryStudy(models.Model):
    categoria_estudio = models.CharField(
        max_length=200, 
        verbose_name="Categoria de estudio"
    )
    created = models.DateField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta():
        verbose_name = "Categoria de estudio"
        verbose_name_plural = 'Categorias de estudio'
        ordering = ['created']

    def __str__(self):
        return self.categoria_estudio

class CategoryManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = ( # Q(cat_estudio__icontains=query) 
                        Q(name__icontains=query) 
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


@python_2_unicode_compatible
class Category(models.Model):  
    cat_estudio = models.ForeignKey(
        CategoryStudy, 
        on_delete=models.CASCADE, 
        verbose_name='Categorias de estudio', 
        related_name='categoriasEstudio'
    )

    name = models.CharField(
        max_length=200, 
        verbose_name="Categoria",
        null='True'
    )

    catest = models.ManyToManyField(
        'self',
        blank=True,
        related_name='category_m2m',
        verbose_name='Revisa categorias'
    )

    for_inline = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='inline_test_models_rf'
    )

    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CategoryManager()

    class Meta():
        verbose_name = "Palabra clave"
        verbose_name_plural = 'Palabras Claves'
        ordering = ['created']

    def __str__(self):
        return self.name


class BookManager(models.Manager):
    def search(self, query):
        qs = self.get_queryset()

        if query is not None:
            or_lookup = (Q(titulo__icontains=query) | 
                         Q(autor__icontains=query) |
                         Q(editorial__icontains=query) |
                        Q(categorias__name__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

    def rel_search(self, rel):
        qs = self.get_queryset()
        
        if rel is not None:
            or_lookup = (
                        Q(categorias__name__icontains=rel)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class Book(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    titulo = models.CharField(
        max_length=200, 
        verbose_name='Título',
    )
    autor = models.CharField(
        max_length=200, 
        verbose_name='Autor', 
        null=True
    )
    descripcion = RichTextField(
        verbose_name='Escribe aquí una breve descripción del libro', 
        max_length=8000
    )
    imagen = models.ImageField(
        verbose_name="portada del libro", 
        upload_to='nodos'
    )
    isbn = models.FloatField(
        verbose_name='Introduce el ISBN', 
        blank=True, null=True ,
        max_length=13, 
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    editorial = models.CharField(
        max_length=200, 
        verbose_name='Editorial',
        null=True
    )
    procedencia = RichTextField(
        max_length=200, 
        verbose_name='Procendencia',
        null=True
    )
    year = models.IntegerField(
        verbose_name="Año de edición", 
        blank=True, 
        null=True
    )
    link_texto = models.CharField(
        max_length=15, 
        verbose_name='Texto del link', 
        null=True, 
        blank=True
    )
    link = models.URLField(
        verbose_name='link', 
        null=True, 
        blank=True
    )
    usuario = models.ForeignKey(User, 
        verbose_name='Usuario', 
        blank =True, 
        null=True, 
        on_delete=models.PROTECT
    )

    # Categorías de Estudio

    cate_estudio = models.ManyToManyField(
        'nodos.CategoryStudy',   
        verbose_name='Categorías de estudio',
        help_text='Seleccione las categorías de estudio que contine el libro.',
        related_name='get_cat_estudy'
    )

    categorias = models.ManyToManyField(
        'nodos.Category', 
        verbose_name='Relaciones', 
        related_name='get_nodos'
    )
    resumen = RichTextField(
        verbose_name='Resumen', 
        null=True, 
        blank=True
    )
    # Línea del tiempo
    PERIODO = (
        ('00', '1900'),
        ('10', '1910'),
        ('20', '1920'),
        ('30', '1930'),
        ('40', '1940'),
        ('50', '1950'),
        ('60', '1960'),
        ('70', '1970'),
        ('80', '1980'),
        ('90', '1990'),
        ('2m', '2000'),
        ('21', '2010'),
        ('22', '2020'),
    )

    periodo = MultiSelectField(
        max_length=60,  
        choices=PERIODO, 
        default='00', 
        verbose_name='Periódo de tiempo',
        help_text='Seleccione las décadas que abarca el libro.'
    )


    # Mapas
    pais = models.CharField(
        max_length=20, 
        default='México', 
        verbose_name='País y/o Edo'
    )
    mapWidth = models.FloatField(
        verbose_name='Introduce el ancho del marcador (círculo), en el mapa', 
        default="15" ,
        max_length=2, 
        help_text='Entre 15 - 65'
    )
    mapHeight = models.FloatField(
        verbose_name='Introduce el ancho del marcador (círculo), en el mapa', 
        default="15" ,
        max_length=2, 
        help_text='Entre 15 - 65'
    )
    long = models.FloatField(
        verbose_name='Introduce la longitud', 
        blank=True, 
        null=True ,
        max_length=13, 
        help_text='longitud <a href="https://www.bufa.es/google-maps-latitud-longitud/">Obteber longitud</a>'
    )
    lat = models.FloatField(
        verbose_name='Introduce la latitud', 
        blank=True, 
        null=True ,
        max_length=13, 
        help_text='latitud <a href="https://www.bufa.es/google-maps-latitud-longitud/">Obtener latitud</a>'
    )
    created = models.DateField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
        )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de Edición'
    )
    objects = BookManager()

    class Meta:
        verbose_name='Libro'
        verbose_name_plural = 'Libros'
        ordering = ['created']

    def __str__(self):
        return self.titulo

    def lista_categorias(self):
        return ', '.join([ categorias.name for categorias in self.categorias.all()[:4] ])
        lista_categorias.short_description = 'Categorias'



class TModel(models.Model):
    name = models.CharField(
    max_length=200,         
    verbose_name='Título')

    def __str__(self):
        return self.name


        