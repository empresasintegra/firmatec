# Generated by Django 3.2.3 on 2021-09-20 13:22

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_auto_20210913_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='provincia', null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.ciudad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='provincia',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='region', null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.provincia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='representante_legal',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut_representante',
            field=models.CharField(blank=True, error_messages={'unique': 'Ya existe un representante legal con este RUT registrado.'}, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='planta',
            name='ciudad',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='provincia', null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.ciudad'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='provincia',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='region', null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.provincia'),
        ),
    ]
