# Generated by Django 2.0.2 on 2018-07-10 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('autor', models.CharField(max_length=200, null=True, verbose_name='Autor')),
                ('descripcion', models.TextField(verbose_name='Escribe aquí una breve descripción del libro')),
                ('imagen', models.ImageField(upload_to='project', verbose_name='portada del libro')),
                ('isbn', models.FloatField(blank=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, null=True, verbose_name='Introduce el ISBN')),
                ('editorial', models.CharField(max_length=200, null=True, verbose_name='Editorial')),
                ('procedencia', models.TextField(max_length=200, null=True, verbose_name='Procendencia')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name="Introduce el año, ej. '1984'")),
                ('link_texto', models.CharField(blank=True, max_length=15, null=True, verbose_name='Texto del link')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
                ('resumen', models.TextField(blank=True, max_length=600, null=True, verbose_name='Resumen')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categorias',
            field=models.ManyToManyField(related_name='get_nodos', to='nodos.Category', verbose_name='Relaciones'),
        ),
        migrations.AddField(
            model_name='book',
            name='usaurio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
