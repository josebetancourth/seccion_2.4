from django.db import models

class materia(models.Model):
    
    idmateria=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    carrera=models.CharField(max_length=20)
    semestre=models.CharField(max_length=20)
    