# Generated by Django 4.1 on 2022-11-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('idmateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('carrera', models.CharField(max_length=20)),
                ('semestre', models.CharField(max_length=20)),
            ],
        ),
    ]
