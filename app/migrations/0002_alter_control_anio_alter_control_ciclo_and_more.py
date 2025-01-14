# Generated by Django 5.1.3 on 2024-11-25 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='anio',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='ciclo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='clasificacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='codigo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='compania',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='conclusion_diseno',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='descripcion_control',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='descripcion_riesgo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='fecha_elaboracion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='frecuencia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='horas_invertidas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='id_estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.estado'),
        ),
        migrations.AlterField(
            model_name='control',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AlterField(
            model_name='control',
            name='naturaleza',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='objetivo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='recursos_consultados',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='semestre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='supervisor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='tipologia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
