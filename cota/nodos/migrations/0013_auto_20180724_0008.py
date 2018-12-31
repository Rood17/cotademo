# Generated by Django 2.0.2 on 2018-07-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0012_auto_20180723_2130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_estudio',
            field=models.CharField(choices=[('PD', 'Período'), ('LA', 'Lugar'), ('PE', 'Personajes'), ('PO', 'Proyectos'), ('IE', 'Instituciones'), ('CO', 'Conceptos/Ideas'), ('DA', 'Diciplinas'), ('AO', 'Acontecimientos'), ('EO', 'Estilos/Corrientes'), ('ME', 'Materiales/Tecnologías'), ('AA', 'Ausencias'), ('OA', 'Palabras Oscuras')], default='PD', max_length=2, verbose_name='Categorias de estudio'),
        ),
    ]