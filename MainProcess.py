import requests

#url de la api
api_url = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"

#obtenemos TODOS los datos de la api
response=requests.get(api_url)

# Convierte la respuesta en un diccionario de Python
data = response.json()

# Define el país que deseas buscar
pais_a_buscar = "Argentina"

# Inicializa una lista vacía para almacenar los valores
valores = []

for item in data[1]:  # data[1] contiene los datos reales, data[0] contiene metadatos
    # Comprueba si el valor del país coincide con el país que deseas buscar
    if item["country"]["value"] == pais_a_buscar:
        # Si el valor no es None, lo añade a la lista
        if item["value"] is not None:
            valores.append(item["value"])

# Imprime los valores
print(valores)

