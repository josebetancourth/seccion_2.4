from django.db import models

class profesor(models.Model):
   cedula=models.IntegerField(primary_key=True) 
   nombre=models.CharField(max_length=30)
   apellido=models.CharField(max_length=30)
   titulo=models.CharField(max_length=20)
   
class materia(models.Model):
    codmateria=models.IntegerField(primary_key=True)
    nomateria=models.CharField(max_length=20)
    facultad=models.CharField(max_length=20)
    semestre=models.CharField(max_length=20)
    
class curso(models.Model):
    codcurso=models.IntegerField(primary_key=True)
    idprofesor=models.ForeignKey(profesor,on_delete=models.CASCADE)
    idmateria=models.ForeignKey(materia,on_delete=models.CASCADE)
    hora=models.CharField(max_length=10)
    
class alumno(models.Model):
    idalumno=models.IntegerField(primary_key=True)
    nomalumno=models.CharField(max_length=20)
    apealumno=models.CharField(max_length=20)
    idcurso=models.ForeignKey(curso,on_delete=models.CASCADE)

