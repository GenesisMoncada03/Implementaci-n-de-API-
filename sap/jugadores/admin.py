from django.contrib import admin
# Register your models here.
from jugadores.models import Plataforma, Juego, Jugador, GeneroJuego, Modo

admin.site.register(Jugador)
admin.site.register(Juego)
admin.site.register(Plataforma)
admin.site.register(Modo)
admin.site.register(GeneroJuego)