from __future__ import unicode_literals
from django.db import models
from datetime import date,datetime

# TODO Añadiendo validaciones
# Nuestro administrador personalizado!
# Ningún método en nuestro nuevo administrador debería recibir el objeto de solicitud completo como argumento!
# (solo partes, como request.POST)
# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        # if postData['title_show'] in :
        #     errors["title_show"] = "El SHOW ya existe"

        hoy = date.today()
        fecha_formulario = datetime.strptime(postData['date_show'], "%Y-%m-%d").date()

        if fecha_formulario >= hoy:
            errors["date_show"] = "La fecha debe ser menor al dia de hoy"

        # if postData['date_show'] == str(date.today()):
        #     errors["date_show"] = "La fecha debe ser distinta al dia de hoy"

        if len(postData['title_show']) < 2:
            errors["title_show"] = "El TITULO del show debe tener al menos 2 caracteres"
        if len(postData['network_show']) < 3:
            errors["network_show"] = "Network debe tener al menos 3 caracteres"
        if len(postData['desc_show']) >0:
            if len(postData['desc_show']) <10:
                errors["desc_show"] = "La DESCRIPCION debe tener al menos 10 caracteres"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45, unique=True)
    network = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True) #hacemos datos opcional
    release_date = models.DateField(default='1999-01-01')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() #se añade esto para la validacion