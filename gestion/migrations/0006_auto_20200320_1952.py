# Generated by Django 3.0.2 on 2020-03-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_estudiante_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(upload_to='perfiles'),
        ),
    ]