# Generated by Django 3.0.2 on 2020-03-25 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_remove_observaciones_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observaciones',
            old_name='ramos',
            new_name='ramo',
        ),
    ]
