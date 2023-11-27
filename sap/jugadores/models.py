from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.nombre

class Modo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class GeneroJuego(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    sexo = [
        ("M", "Masculino"),
        ("F", "Femenino")
    ]

    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=sexo, null=True)
    Email = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    fecha_de_inicio = models.DateField(null=True)
    modos_preferidos = models.ForeignKey(Modo, on_delete=models.SET_NULL, null=True)
    generos_preferidos = models.ForeignKey(GeneroJuego, on_delete=models.SET_NULL, null=True)
    plataforma_preferida = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True)
    juego_preferido = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


