from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Task2(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - by  ' + self.user.username

class Persona(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    dni = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Ingreso(models.Model):
    motivo = models.CharField(max_length=200)
    importe = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.motivo
    
class Egreso(models.Model):
    motivo = models.CharField(max_length=200)
    importe = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.motivo