# Generated by Django 3.0.2 on 2020-03-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_auto_20200322_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles_profesores/'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles_profesores/'),
        ),
    ]