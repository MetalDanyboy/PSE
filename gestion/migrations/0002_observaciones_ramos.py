# Generated by Django 3.0.2 on 2020-03-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observaciones',
            name='ramos',
            field=models.CharField(choices=[('Matemáticas', 'Matemáticas'), ('Lenguaje', 'Lenguaje'), ('Historia', 'Historia'), ('Ciencias', 'Ciencias'), ('Inglés', 'Inglés'), ('Artes', 'Artes'), ('Taller', 'Taller'), ('Música', 'Música'), ('Ed. Física', 'Ed. Física')], default='Matemáticas', max_length=50),
        ),
    ]