import ctypes

#import requests
#api_url = "https://jsonplaceholder.typicode.com/todos/1"
#response=requests.get(api_url)
#print(response.json())

#creamos una biblioteca de objetos. Dynamic Link Library(DLL)
clibrary = ctypes.CDLL("/home/gaston/Documentos/SdC_Proyectos/SistDeCompTP2/ctypes/clibrary.so")

clibrary.display()