import ctypes
#import os

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response=requests.get(api_url)
print(response.json())

#creamos una biblioteca de objetos. Dynamic Link Library(DLL)
clibrary = ctypes.CDLL("/home/gaston/Documentos/SdC_Proyectos/SistDeCompTP2/ctypes/clibrary.so")

#convertimos la cadena string en una secuencia binaria(en un objeto de bytes)
#clibrary.display(b"gaston",23)

#asiganamos nombre a la funcion
func= clibrary.display

#argtypes tiene los tipos argumentos que son los q necesita la funcion func. es una lista de argumentos, ya q pueden haber varios
func.argtypes = [ctypes.c_char_p,ctypes.c_int]
#definimos el tipo de retorno de la funcion. solo puede un tipo de retorno,por lo tanto no ponemos entre [](osea una lista). char_p: puntero caracter
func.restype = ctypes.c_char_p

#creamos un buffer para alli almacenar la informacion
string = ctypes.create_string_buffer(100)
string.value=b"gaston"

clibrary.display(string,23)

####
#asiganamos nombre a la funcion
alloc_func=clibrary.alloc_memory
#definimos el tipo de retorno de la funcion. es un puntero. osea decimos que queremos un PUNTERO de la clase char
alloc_func.restype=ctypes.POINTER(ctypes.c_char_p)

#asiganamos nombre a la otra funcion
free_func=clibrary.free_memory
##definimos el argumento de la funcion
free_func.argtypes=[ctypes.POINTER(ctypes.c_char_p)]

cstring_pointer = alloc_func()
cstring = ctypes.c_char_p.from_buffer(cstring_pointer)
print(cstring.value)
free_func(cstring_pointer)

## para crear un puntero en python:
#aca lo creamos, del tipo int
ptr2 = ctypes.POINTER(ctypes.c_int)
#aca ponemos a que apunta
num=ctypes.c_int(100)
ptr2.contents=num
print(ptr2.contents)


##obtenemos el directorio de trabajo actual
#path = os.getcwd()
#clibrary = ctypes.CDLL(os.path.join(path,'clibrary.so'))
###creamos una matriz y se la vamos a pasar a C,luego C nos va a devolver una suma q va a hacer con esa matriz
##creamos la matriz
values = (ctypes.c_int*10)()
for i in range(len(values)):
    values[i]=i

#le pasamos los argumentos a la funcion de c
sum=clibrary.sumArray(values,len(values))
print("suma: ",sum)

##ahora al reves, creamos una matriz en C y se la pasamos a python
#espeficamos el retorno de la funcion de c que vamos a utilizar,que nos va a mandar un array
clibrary.incArray.restype = ctypes.POINTER(ctypes.c_int)
result=clibrary.incArray(values,len(values))
for i in range(10):
    print(result[i])
    
    
#recibir una matriz desde C y guardarla como un python object(una lista)
clibrary.getArray.restype=ctypes.POINTER(ctypes.c_int)
result = clibrary.getArray()

mylist = result[0:10]
print(mylist)

clibrary.free_memory2(result)