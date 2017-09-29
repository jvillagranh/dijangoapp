from django.contrib import admin

# Register your models here.
from.models import Preguntas
from.models import Opciones

admin.site.register(Preguntas)
admin.site.register(Opciones)
