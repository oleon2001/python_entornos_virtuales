import requests  # Importar la biblioteca requests para realizar solicitudes HTTP

def get_categories():  # Definir una función para obtener categorías de la API
    r = requests.get('https://api.escuelajs.co/api/v1/categories')  # Enviar solicitud GET a la API para obtener categorías
    print(r.status_code)  # Imprimir código de estado de la respuesta
    
    # La respuesta es un objeto Response de requests, que contiene información sobre la respuesta
    print(r.text)  # Imprimir texto plano de la respuesta (datos devueltos por la API)
    print(type(r.text))  # Imprimir tipo de datos de la respuesta (str, bytes, etc.)
    
    # El método json() de la respuesta permite parsear la respuesta como JSON
    categories = r.json()  # Parsear respuesta como JSON y almacenar en la variable categories
    
    # Iterar sobre las categorías y imprimir su nombre
    for x in categories:  
        print(x['name'])  # Imprimir valor de la clave 'name' para cada categoría