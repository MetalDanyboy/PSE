# Generated by Django 3.0.2 on 2020-01-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Profesores',
        ),
        migrations.DeleteModel(
            name='Articulos',
        ),
        migrations.RenameField(
            model_name='profesores',
            old_name='tfno',
            new_name='telefono',
        ),
    ]
