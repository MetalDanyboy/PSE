# Generated by Django 3.0.2 on 2020-03-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20200325_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='observacion',
            field=models.TextField(max_length=500),
        ),
    ]