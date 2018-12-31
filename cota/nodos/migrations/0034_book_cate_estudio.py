# Generated by Django 2.0.2 on 2018-11-07 19:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0033_auto_20181105_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cate_estudio',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('01', 'Palabras oscuras'), ('02', 'Diciplinas'), ('03', 'Periódo del tema'), ('04', 'Lugar del tema'), ('05', 'Personajes'), ('06', 'Proyectos'), ('07', 'Instituciones'), ('08', 'Conceptos o ideas'), ('09', 'Acontecimientos históricos'), ('10', 'Estilos o corrientes'), ('11', 'Materiales o tecnologías'), ('12', 'Ausencias')], default='01', help_text='Seleccione las categorías de estudio que contine el libro.', max_length=60, verbose_name='Categorías de estudio'),
        ),
    ]