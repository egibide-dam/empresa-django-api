# Generated by Django 5.0.4 on 2024-04-10 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'habilidad',
                'verbose_name_plural': 'habilidades',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('antiguedad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresaDjango.departamento')),
                ('habilidad', models.ManyToManyField(to='appEmpresaDjango.habilidad')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'ordering': ['-created'],
            },
        ),
    ]
