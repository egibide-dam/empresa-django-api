# Generated by Django 5.0.4 on 2024-04-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='habilidad',
            field=models.ManyToManyField(null=True, to='appEmpresaDjango.habilidad'),
        ),
    ]