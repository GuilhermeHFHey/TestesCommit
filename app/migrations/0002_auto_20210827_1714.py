# Generated by Django 3.2.5 on 2021-08-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='fumo',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='pesoPreOperatorio',
        ),
        migrations.AddField(
            model_name='pacientes',
            name='alta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='gc',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='altura',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='ano1',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='ano2',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='ano3',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='ano4',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='ano5',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='cx',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='imc',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='mes1',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='mes3',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='mes6',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='mes9',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='tpo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]