# Generated by Django 3.2.3 on 2021-09-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_alter_planta_rut_representante'),
        ('ficheros', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichero',
            name='Clientes',
            field=models.ManyToManyField(to='utils.Cliente'),
        ),
    ]