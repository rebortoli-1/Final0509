from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):

    nombre=models.CharField(max_length=40)
    devops= models.BooleanField

    def __str__(self):
        return f"Nombre: {self.nombre} - devops {self.devops}"

class Metrica(models.Model):
    nombre= models.CharField(max_length=30)
    proyecto_ref= models.ForeignKey(Proyecto,on_delete=models.PROTECT)
    def __str__(self):
        return f"Nombre: {self.nombre} - Proyecto {self.proyecto_ref}"

class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

