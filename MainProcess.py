import requests
import ctypes

# url de la api
api_url = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"

# obtiene TODOS los datos de la api
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

# crea una biblioteca de objetos. Dynamic Link Library(DLL)
clibrary = ctypes.CDLL("/home/gaston/Documentos/SdC_Proyectos/SistDeCompTP2/ctypes/clibrary.so")

# asigana nombre a la funcion
func = clibrary.ChangesArray

# Define el tipo de los argumentos y el valor de retorno de la función
func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
func.restype = ctypes.POINTER(ctypes.c_int)

# Crea un array de C de valores float a partir de la lista de Python
valores_c = (ctypes.c_float * len(valores))(*valores)

# Llama a la función de c. nuevosvalores_c es un puntero a la memoria que fue asignada en la función ChangesArray del código de C para almacenar el nuevo array de ints.
nuevosvalores_c = func(valores_c, len(valores))

# Convierte el resultado a una lista de Python(un objeto python)
valores_po = nuevosvalores_c[:len(valores)]
print(valores_po) 

#liberar memoria. llama a funcion de programa en c.
clibrary.free_memory(nuevosvalores_c)
