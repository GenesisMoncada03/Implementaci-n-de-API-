from rest_framework import serializers

from jugadores.models import Jugador, Juego, Modo, GeneroJuego, Plataforma


class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugador
        fields = ('url','id','nombre', 'sexo', 'Email', 'juego_preferido', 'plataforma_preferida', 'generos_preferidos',
            'modos_preferidos','fecha_de_inicio', 'activo')
class JuegoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Juego
        fields = ('url','id','nombre')

class PlataformaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plataforma
        fields = ('url','id','nombre')


class ModoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modo
        fields = ('url', 'id', 'nombre')


class GeneroJuegoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroJuego
        fields = ('url', 'id', 'nombre')