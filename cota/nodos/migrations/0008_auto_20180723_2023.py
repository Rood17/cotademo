# Generated by Django 2.0.2 on 2018-07-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0007_auto_20180723_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_estudio',
            field=models.CharField(choices=[('PO', 'Período'), ('LU', 'Lugar'), ('PS', 'Personajes'), ('IS', 'Instituciones')], default='PO', max_length=2),
        ),
    ]
