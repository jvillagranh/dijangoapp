from django.db import models

# Create your models here.
class Preguntas(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return str(self.id) + " - " + self.pregunta_texto


class Opciones(models.Model):
    pregunta = models.ForeignKey(Preguntas)
    opcion_texto = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcion_texto
