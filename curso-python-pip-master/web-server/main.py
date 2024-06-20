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
        <p>TE ODIO CON TODAS LAS FUERZAS QUE UN HOMBRE PUEDE ODIAR- PEGATE</p>
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

 correr el servidor de uvicorn

 uvicorn main:adrianTeOdio --reload

 main es el archivo donde se esta ejecutando
 adrianTeOdio es el objeto que contiene al fastApi para hacer las peticiones
 --reload es para que se reinicie el servidor cada vez que se hace un cambio en el código
 

'''


'''
añadidos adicionales



    FastAPI

    Es un framework de Python para crear aplicaciones web
      rápidas y seguras. Utilice la mejor OpenAPI para definir la 
      interfaz de la aplicación y proporcione un conjunto de herramientas
        para validar y documentar la API de manera automática.

    ****Uvicorn ****

    Es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento 
    para ejecutar aplicaciones ASGI como FastAPI. Es una alternativa a otros servidores ASGI 
    como Daphne y Hypercorn.

    FastAPI y Uvicorn se utilizan 
    juntos para proporcionar un entorno rápido y fácil de usar 
    para el desarrollo y el uso de aplicaciones web basadas en ASGI.

'''


'''
un endpoint es una URL específica que una aplicación utiliza para interactuar con el 
cliente (usualmente un navegador web o una aplicación móvil) para realizar una acción específica o recuperar datos específicos.

Piensa en un endpoint como una puerta de entrada a un recurso o funcionalidad específica dentro de una a
plicación. Cuando un cliente (como un navegador web) envía una solicitud a un endpoint, la aplicación procesa
la solicitud y devuelve una respuesta, que puede ser en forma de datos, HTML, JSON o incluso un mensaje de error.

En el código proporcionado, tenemos dos endpoints:

@adrianTeOdio.get('/') - Este endpoint se define en la URL raíz (/) y devuelve una lista de enteros [1, 2, 3].
@adrianTeOdio.get('/contact', response_class=HTMLResponse) - Este endpoint se define en 
la URL /contact y devuelve una respuesta HTML con un título y un párrafo.
Los endpoints se pueden definir utilizando diferentes métodos HTTP, como:

GET: Recupera datos del servidor.
POST: Envía datos al servidor para crear un nuevo recurso.
PUT: Actualiza un recurso existente en el servidor.
DELETE: Elimina un recurso en el servidor.
En FastAPI, los endpoints se definen utilizando decoradores, 
como @app.get('/') o @app.post('/create'), que especifican el método HTTP y la ruta URL para el endpoint.

'''
