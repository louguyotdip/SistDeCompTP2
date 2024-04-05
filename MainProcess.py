import ctypes

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response=requests.get(api_url)
print(response.json())

#creamos una biblioteca de objetos. Dynamic Link Library(DLL)
clibrary = ctypes.CDLL("/home/gaston/Documentos/SdC_Proyectos/SistDeCompTP2/ctypes/clibrary.so")

#convertimos la cadena string en una secuencia binaria
#clibrary.display(b"gaston",23)

#asiganamos nombre a la funcion
func= clibrary.display

#argtypes tiene los tipos argumentos. es una lista de argumentos, ya q pueden haber varios
func.argtypes = [ctypes.c_char_p,ctypes.c_int]
#definimos el tipo de retorno de la funcion. solo puede un tipo de retorno,por lo tanto no ponemos entre [](osea una lista)
func.restype = ctypes.c_char_p
clibrary.display(b"gaston",23)