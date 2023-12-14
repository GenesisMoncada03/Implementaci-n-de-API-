import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

nombre = []
sexo = []
juego_preferido = []
plataforma_preferida = []
modo_preferido = []

url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table')
filas = tabla.find_all('tr')

for fila in filas:
    celdas = fila.find_all('td')

    if not celdas:
        continue

    nombre.append(celdas[0].get_text(strip=True))
    sexo.append(celdas[1].get_text(strip=True))
    juego_preferido.append(celdas[2].get_text(strip=True))
    plataforma_preferida.append(celdas[3].get_text(strip=True))
    modo_preferido.append(celdas[4].get_text(strip=True))

# Crear un DataFrame de pandas
df = pd.DataFrame({
    'Nombre': nombre,
    'Sexo': sexo,
    'Juego preferido': juego_preferido,
    'Plataforma preferida': plataforma_preferida,
    'Modo preferido': modo_preferido
})

# Imprimir el DataFrame como tabla si se creó correctamente
if 'df' in locals() or 'df' in globals():
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
else:
    print("Error: No se pudo crear el DataFrame.")

# Guardar el DataFrame en un archivo CSV
df.to_csv('Jugadores.csv', index=False, encoding='utf-8')

print("Datos guardados exitosamente en Jugadores.csv.")
print("Vuelva Pronto :)")