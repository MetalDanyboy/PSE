# Generated by Django 3.0.2 on 2020-03-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_remove_estudiante_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='nom_usuario',
            field=models.CharField(default='usuario', max_length=50),
            preserve_default=False,
        ),
    ]
