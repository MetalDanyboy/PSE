# Generated by Django 3.0.2 on 2020-03-25 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20200325_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='titulo',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='observacion',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.RemoveField(
            model_name='notas',
            name='assignment',
        ),
        migrations.AddField(
            model_name='notas',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.Assignment'),
            preserve_default=False,
        ),
    ]
