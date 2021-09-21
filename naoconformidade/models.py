from django.db import models
import geocoder



class NC (models.Model):
    Municipio = models.CharField(max_length= 30)
    TN = models.CharField(max_length=20)
    Descricao = models.CharField(max_length=140, null= True)
    Unidade = models.CharField (max_length=20, null=True)
    Prazo = models.DateField(null=True)
    TipoSituacao = (
        ('A','Atendida'),
        ('P', 'Pendente'),

    )
    Situacao = models.CharField(max_length=1, choices=TipoSituacao, null=True)
    OBS = models.CharField(max_length=40, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)





    class Meta:
        verbose_name_plural = 'NC'
    def save(self,*args,**kwargs):
        self.latitude = geocoder.osm(self.Municipio).lat
        self.longitude = geocoder.osm(self.Municipio).lng
        return super().save(*args,**kwargs)


    def __str__(self):
        return self.Municipio

class Alert (models.Model):
    alert_date = models.DateField()

