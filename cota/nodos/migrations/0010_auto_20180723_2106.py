# Generated by Django 2.0.2 on 2018-07-24 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0009_auto_20180723_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name': 'Sub Categoria', 'verbose_name_plural': 'Sub Categorias'},
        ),
        migrations.AlterModelOptions(
            name='categorystudy',
            options={'ordering': ['created'], 'verbose_name': 'Categoria de estudio', 'verbose_name_plural': 'Categorias de estudio'},
        ),
    ]
