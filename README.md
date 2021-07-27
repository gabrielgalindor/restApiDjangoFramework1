# Prueba Tech de Django

Este es un proyecto de prueba, que permite leer las entradas de una "supuesta tarjeta de crédito" que solicita de manera aleatoria 3 caracteres. Si la contraseña es 531278, el banco puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la secuencia 3-1-7.


# Instalación del proyecto

Para instalar el proyecto puede realizar un git Clone del mismo y deberá contener los paquetes:

> Django==3.2.5
> djangorestframework==3.12.4
> PyMySQL==1.0.2


## Instalación de paquetes por virtualenv

El proyecto cuenta con un entorno virtual que contiene estos paquetes. **Tenga en cuenta que si opta por este entorno, hay una carpeta llamada "card" que contiene dos modulos que realizan la lógica de decifrar los números de la tarjeta según las entradas puestas**. Estos dos modulos también se encuentran dentro de la app de *"restapidjango"*.  O si desea crear su propio entorno virtual, también puede leer el archivo de requirements.txt. 