# Generated by Django 2.0.2 on 2018-07-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0002_auto_20180709_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='imagen',
            field=models.ImageField(upload_to='project', verbose_name='portada del libro'),
        ),
        migrations.AlterField(
            model_name='book',
            name='resumen',
            field=models.TextField(blank=True, null=True, verbose_name='Resumen'),
        ),
    ]