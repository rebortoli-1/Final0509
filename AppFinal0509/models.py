from asyncio.windows_events import NULL
from email.policy import strict
from multiprocessing import Value
from pyexpat import model
import string
from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):

    nombre=models.CharField(max_length=40)
    jefatura=models.CharField(max_length=40)
    gerencia=models.CharField(max_length=40)
    devops=models.BooleanField()
   
    def __str__(self):
        return f"Nombre: {self.nombre} - Jefatura {self.jefatura} - Gerencia {self.gerencia} - Devops {self.devops}"

class Metrica(models.Model):
    nombre= models.CharField(max_length=30)
    proyecto_ref= models.ForeignKey(Proyecto,on_delete=models.PROTECT)
    observacion=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Proyecto {self.proyecto_ref} - Observacion{self.observacion}"

class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

