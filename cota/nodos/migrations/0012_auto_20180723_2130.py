# Generated by Django 2.0.2 on 2018-07-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0011_auto_20180723_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias de estudio'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='categorias_estudio',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_estudio',
            field=models.CharField(choices=[('PD', 'Período'), ('LA', 'Lugar'), ('PE', 'Personajes'), ('PO', 'PROYECTOS'), ('IE', 'Instituciones'), ('CO', 'Conceptos/Ideas'), ('DA', 'Diciplinas'), ('AO', 'Acontecimientos'), ('EO', 'Estilos/Corrientes'), ('ME', 'Materiales/Tecnologías'), ('AA', 'Ausencias'), ('OA', 'Palabras Oscuras')], default='PD', max_length=2),
        ),
        migrations.DeleteModel(
            name='CategoryStudy',
        ),
    ]