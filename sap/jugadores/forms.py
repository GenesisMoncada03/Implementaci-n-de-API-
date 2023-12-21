from django import forms
from jugadores.models import Jugador


class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = (
            'nombre', 'sexo', 'Email', 'juego_preferido', 'plataforma_preferida', 'generos_preferidos',
            'modos_preferidos',
            'fecha_de_inicio', 'activo')
        widgets = {
            'Email': forms.EmailInput(attrs={'type': 'email'}),
            'fecha_de_inicio': forms.DateInput(attrs={'type': 'date'}),
        }