# Generated by Django 4.1 on 2022-11-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('carrera', models.CharField(max_length=15)),
                ('semestre', models.CharField(max_length=15)),
            ],
        ),
    ]