import requests
import ctypes
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# URL de la api
api_url = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"

# Obtiene TODOS los datos de la api
def valueget():
    response = requests.get(api_url)
    return response

# Convierte la respuesta en un diccionario de Python
data = valueget().json()

# Define el país que se desea buscar
pais_a_buscar = "Argentina"

# Inicializa una lista vacía para almacenar los valores
valores = []
# Inicializa una lista vacía para almacenar los años de la lista de valores
anios = []

# Inicializa una lista vacía para almacenar los valores
for item in data[1]:  # data[1] contiene los datos reales, data[0] contiene metadatos
    # Comprueba si el valor del país coincide con el país que se desea buscar
    if item["country"]["value"] == pais_a_buscar:
        # Si el valor no es None, se añade a la lista
        if item["value"] is not None:
            valores.append(item["value"])
            anios.append(item["date"])

# Imprime los valores
print(valores)
print(anios)

# Crea una biblioteca de objetos. Dynamic Link Library(DLL)
clibrary = ctypes.CDLL("/home/federica/Documents/Sistemas_de_Computacion/practico_2/SistDeCompTP2/ctypes/clibrary.so")

# Asigna nombre a la funcion
func = clibrary.ChangesArray

# Define el tipo de los argumentos y el valor de retorno de la función
func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
func.restype = ctypes.POINTER(ctypes.c_int)

# Crea un array de C de valores float a partir de la lista de Python
valores_c = (ctypes.c_float * len(valores))(*valores)

# Llama a la función de c. nuevosvalores_c es un puntero a la memoria que fue asignada en la función ChangesArray del código de C para almacenar el nuevo array de ints.
nuevosvalores_c = func(valores_c, len(valores))

# Convierte el resultado a una lista de Python (un objeto python)
valores_po = nuevosvalores_c[:len(valores)]
print(valores_po) 

# Crea una lista de índices para el eje y
#indices = list(range(len(valores_po)))

# Crea el gráfico
#plt.plot(anios, valores_po)
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
plt.grid(True)
plt.plot(anios, valores_po, color = 'blue', linewidth = 2, linestyle = '-.')
plt.title("Cambio de valores de GINI - Argentina")
plt.ylim(20, 60)

# Etiqueta los ejes
plt.xlabel("Año")
plt.ylabel("Valor de GINI")

# Ajusta los margenes del grafico
plt.subplots_adjust(bottom=0.2, right=0.85)

# Crea el botón
button = plt.axes([0.75, 0.05, 0.2, 0.075])  # Posición y tamaño del botón
btn = Button(button, 'Guardar imagen', color = 'lightblue')

# Función que se ejecutará cuando se presione el botón
def on_button_clicked(event):
    plt.savefig("Cambio_de_valores_de_GIN_Argentina.png")
    print('Imagen guardada!')

# Conecta la función al evento del botón
btn.on_clicked(on_button_clicked)

# Muestra el gráfico
plt.show()

# Libera la memoria. Llama a funcion de programa en C.
clibrary.free_memory(nuevosvalores_c)
