from django.db import models

class materia(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=15)
    carrera=models.CharField(max_length=15)
    semestre=models.CharField(max_length=15)
    

