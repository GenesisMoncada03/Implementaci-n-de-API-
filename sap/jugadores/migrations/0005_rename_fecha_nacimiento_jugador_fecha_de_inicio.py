# Generated by Django 4.2.7 on 2023-11-26 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0004_remove_jugador_generos_preferidos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jugador',
            old_name='fecha_nacimiento',
            new_name='fecha_de_inicio',
        ),
    ]