# Importamos el módulo 'store' que contiene funciones para interactuar con una tienda
import store

# Importamos el framework 'FastAPI' para construir APIs
from fastapi import FastAPI

# Importamos la clase 'HTMLResponse' para devolver respuestas HTML
from fastapi.responses import HTMLResponse

# Creamos una instancia de la aplicación FastAPI
adrianTeOdio = FastAPI()

# Definimos un endpoint GET en la raíz del sitio web ('/') que devuelve una lista de enteros
#Se utiliza para crear una instancia la cual cuando sea mandada a llamar mediante la ruta establecida por una peticion HTTP a una URL ejecutara un función que devolvera un valor dado
'''
La función decoradora @app.get('/') es un ejemplo de un decorador
de ruta en FastAPI. Un decorador de ruta es una forma de definir 
una función que se encargará de manejar una solicitud HTTP específica.
'''

@adrianTeOdio.get('/') # cada que se obtenga la ruta '/' se ejecutara la siguiente funcion
def get_list():
    # Devolvemos una lista de enteros
    return [1, 2, 3]

# Definimos un endpoint GET en la ruta '/contact' que devuelve una respuesta HTML
@adrianTeOdio.get('/contact', response_class=HTMLResponse)
def get_list():
    # Devolvemos una cadena HTML que contiene un título y un párrafo
    return """
        <h1>HOLA ADRIAN :)</h1>
        <p>TE ODIO CON TODAS LAS FUERZAS QUE UN HOMBRE PUEDE ODIAR PEGATE</p>
    """

# Definimos una función 'run' que se ejecutará cuando se ejecute el script
def run():
    # Llamamos a la función 'get_categories' del módulo 'store'
    # Esta función probablemente devuelve una lista de categorías de la tienda
    store.get_categories()

# Verificamos si el script se está ejecutando directamente (no se está importando como módulo)
if __name__ == '__main__':
    # Ejecutamos la función 'run'
    run()

'''
🤖 _Rutina de la clase_👇

__

    Navegar a proyecto Web

cd ../web-server

    Activar ambiente del proyecto

source env/bin/activate 

    Agregar nuevas librerías FastAPI

pip3 install fastapi

    Agregar ASGI (Asynchronous Server Gateway Interface) Uvicorn

pip3 install "uvicorn[standard]"

    Verificar librerías instaladas

pip3 freeze

    Actualizar Requirements

 pip3 freeze > requirements.txt
'''