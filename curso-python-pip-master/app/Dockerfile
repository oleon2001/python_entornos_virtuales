FROM python:3.8 
 # Imagen base para la aplicación, utilizando Python 3.8
# Nota: Esta instrucción indica que se utilizará la imagen oficial de Python 3.8 como base para nuestra aplicación.

WORKDIR /app  
# Establecer el directorio de trabajo en el contenedor en /app
# Nota: Esta instrucción cambia el directorio de trabajo actual en el contenedor a /app, que es donde se instalarán nuestras dependencias y se ejecutará nuestra aplicación.

COPY requirements.txt /app/requirements.txt  
# Copiar el archivo de requisitos en el contenedor
# Nota: Esta instrucción copia el archivo requirements.txt desde el directorio actual en el host (nuestra máquina local) al directorio de trabajo en el contenedor (/app).

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  
# Instalar las dependencias especificadas en requirements.txt
# Nota: Esta instrucción utiliza pip para instalar las dependencias especificadas en el archivo requirements.txt. La opción --no-cache-dir evita que se utilice la caché de pip, y la opción --upgrade garantiza que se instalen las versiones más recientes de las dependencias.

COPY . /app  
# Copiar el directorio actual en el host al contenedor
# Nota: Esta instrucción copia todo el contenido del directorio actual en el host (nuestra máquina local) al directorio de trabajo en el contenedor (/app). Esto incluye nuestro código fuente y cualquier otro archivo necesario para la aplicación.

CMD bash -c "while true; do sleep 1; done"  
# Ejecutar un comando para mantener el contenedor en ejecución indefinidamente
# Nota: Esta instrucción especifica el comando que se ejecutará cuando se inicie el contenedor. En este caso, se utiliza un bucle infinito que duerme durante 1 segundo en cada iteración, lo que mantiene el contenedor en ejecución indefinidamente.