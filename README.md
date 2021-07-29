# Prueba Tech de Django

Este es un proyecto de prueba, que permite leer las entradas de una "supuesta tarjeta de crédito" que solicita de manera aleatoria 3 caracteres. Si la contraseña es 531278, el banco puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la secuencia 3-1-7.


# Instalación del proyecto

El proyecto cuenta con dos maneras de instalarse: 
- Por medio de una imagen hecha en Docker
- Por medio de un entorno virtual que trae consigo el proyecto

## Arrancar la imagen de Dockerfile

El repositorio cuenta con un archivo dockerfile, que le permitirá crear una imagen por defecto para arrancar el proyecto y configurarlo rapidamente. 

Para crear la imagen escriba en su terminal: 

> 
> docker build -t img_ubuntu . --progress=plain
> 

Luego de que termine de construir la imagen "img_ubuntu", es necesario ubicar el nombre de la imagen que se creo en Docker. Así que usted puede ubicar la imagen de docker con el siguiente comando: 

> 
> docker images
> 

Le saldrá una respuesta similar:
> REPOSITORY-----TAG-----IMAGE ID------CREATED-----------SIZE
> img_ubuntu3-----latest-----20afacfbf598-----11 hours ago-----1.13GB
> 

Copie la respuesta de la columna "IMAGE ID" (en el ejemplo sería IMAGE ID= 20afacfbf598). Para correrlo necesita utilizar el siguiente comando:

> 
>  docker run -it [IMAGE ID]
> 

Ya cuando este dentro de la imagen de Ubuntu, si lee el archivo Dockerfile, se dará cuenta que se ha instalado un ambiente de MySQL, es importante entender que cada vez que apague la imagen se borrará toda la información en la base de datos, por lo que se instaló MySQL únicamente para probar que todo está funcionando bien. 



Para instalar el proyecto puede realizar un git Clone del mismo y deberá contener los paquetes:

> Django==3.2.5
> djangorestframework==3.12.4
> PyMySQL==1.0.2

Para instalar los paquetes que trae por defecto el repositorio usted tiene dos opciones: 
- Arrancar la imagen de Docker por medio del dockerfile
- Arrancar el entornovirtual del repositorio


Para configurar la base de datos debe activar el servicio de MySQL con el siguiente comando:

> 
>  service mysql start
>

Para entrar a la terminal de comandos de MySQL puede usar el siguiente comando:

> 
>  mysql -u root
> 

Dentro de MySQL debe escribir las siguientes instrucciones: 

> 
>  CREATE USER 'user5'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password4';
>  GRANT ALL PRIVILEGES ON *.* TO 'user5'@'localhost' WITH GRANT OPTION;
> 
> CREATE USER 'user5'@'%' IDENTIFIED WITH mysql_native_password BY 'password4';
> GRANT ALL PRIVILEGES ON *.* TO 'user5'@'%' WITH GRANT OPTION;

Las instrucciones anteriores permiten que usted pueda crear un usuario (llamado user5) que permitirá acceder a la base de datos de MySQL y tenga todos los privilegios. Ya antes de cerrar la terminal de MySQL, debe crear la base de datos del proyecto: 

> 
>  CREATE DATABASE pruebaehacking;
> 

Ya una vez creada la base de datos, puede cerrar la terminal de MySQL con: 
> 
>  exit
> 

Para iniciar el proyecto de Django, deberá dirigirse a la carpeta de /restApiDjangoFramework1 e iniciar la migración de los datos. Puede realizarlo con el siguiente comando:

> 
>  cd /restApiDjangoFramework1
>  python3 manage.py migrate
> 

Por último, deberá crear un superusuario, lo puede crear con el siguiente comando:
> 
>  py manage.py createsuperuser
> 

Suministre un nombre de usuario, email y contraseña. Debe lucir similar al siguiente:

![](https://i.ibb.co/4fGGDHg/sx1.jpg)

Luego corra el proyecto django con el comando: 
> 
>  py manage.py runserver
>

Luego dirigase a su navegador con la dirección http://127.0.0.1:8000/admin/. Allí haga login con la información proporcionada como superusuaripo. Luego dirigase al link http://127.0.0.1:8000/admin/authtoken/tokenproxy/ y haga clic donde dice add token. Luego en pantalla se le mostrará un token que deberá usar para autenticarse en la API de respuesta. 

Los tokens deberán lucir de manera similar a la siguiente captura de pantalla: 

![](https://i.ibb.co/jTywKjN/sx2.jpg)

Como dije anteriormente, usted deberá usar esta información para poder acceder a la información que le suministrará la API. 

Usted podrá testear la respuesta de la API con el siguiente endpoint:

> 
>  http://127.0.0.1:8000/api/test/
> 

Como dije anteriormente, usted deberá usar esta información para poder acceder a la información que le suministrará la API. 

Agregué en el encabezado de la petición las llaves "USERNAME" y "TOKEN" para generar una autenticación basica (Basic Auth). Y si realizó bien el proceso, la api le deberá generar una respuesta similar a la siguiente: 

![](https://i.ibb.co/3h5yzpF/sx3.jpg)

Y listo, ya está corriendo el servicio y la API. Recuerde que la lógica que se está usando para desencriptar la tarjeta por el archivo "keylog.txt", se encuentra de la carpeta restapidjango>readcard_class.py. En esta clase se compone de los métodos que permiten identificar el orden de los números, que se guía por dos vías:

- La primera es identificando el número que no tiene ningún otro antes del mismo
- La segunda es identificando el número que no tiene ningúnt otro después del mismo

Los une en unos arreglos y luego los compara. 

Las funciones necesarias se encuentran en el modulo readcard_functions.py de la misma carpeta. 


## Instalación de paquetes por virtualenv

El proyecto cuenta con un entorno virtual que contiene estos paquetes. **Tenga en cuenta que si opta por este entorno, hay una carpeta llamada "card" que contiene dos modulos que realizan la lógica de decifrar los números de la tarjeta según las entradas puestas**. Estos dos modulos también se encuentran dentro de la app de *"restapidjango"*.  O si desea crear su propio entorno virtual, también puede leer el archivo de requirements.txt. 

Primero debera instalar virtualenv: 
> 
>  pip install virtualenv
> 

Para iniciar el entorno virtual puede hacer uso del siguiente comando dentro de su terminal ubicandose en la carpeta del proyecto: 

> 
>  envrest\Scripts\Activate
> 

En su terminal de comandos deberá aparecer la línea de comandos normal con un parentesís diciendo "(envrest)".

Tenga en cuenta que para trabajar con el entorno virtual usted deberá instalar MySQL por su cuenta. Sin embargo, esto ofrece la ventaja de que su información no se perderá como en la imagen de Dockerfile. Recuerde crear un usuario llamado "user5" con password="password4". Puede valerse de los pasos anteriormente explicados para realizar la configuración. 

Las instrucciones anteriores permiten que usted pueda crear un usuario (llamado user5) que permitirá acceder a la base de datos de MySQL y tenga todos los privilegios. Ya antes de cerrar la terminal de MySQL, debe crear la base de datos del proyecto: 

> 
>  CREATE DATABASE pruebaehacking;
> 

Ya una vez creada la base de datos, puede cerrar la terminal de MySQL con: 
> 
>  exit
> 

Para iniciar el proyecto de Django, deberá dirigirse a la carpeta de /restApiDjangoFramework1 e iniciar la migración de los datos. Puede realizarlo con el siguiente comando:

> 
>  cd /restApiDjangoFramework1
>  python3 manage.py migrate
> 

Por último, deberá crear un superusuario, lo puede crear con el siguiente comando:
> 
>  py manage.py createsuperuser
> 

Suministre un nombre de usuario, email y contraseña. Debe lucir similar al siguiente:

![](https://i.ibb.co/4fGGDHg/sx1.jpg)

Luego corra el proyecto django con el comando: 
> 
>  py manage.py runserver
>

Luego dirigase a su navegador con la dirección http://127.0.0.1:8000/admin/. Allí haga login con la información proporcionada como superusuaripo. Luego dirigase al link http://127.0.0.1:8000/admin/authtoken/tokenproxy/ y haga clic donde dice add token. Luego en pantalla se le mostrará un token que deberá usar para autenticarse en la API de respuesta. 

Los tokens deberán lucir de manera similar a la siguiente captura de pantalla: 

![](https://i.ibb.co/jTywKjN/sx2.jpg)

Como dije anteriormente, usted deberá usar esta información para poder acceder a la información que le suministrará la API. 

Usted podrá testear la respuesta de la API con el siguiente endpoint:

> 
>  http://127.0.0.1:8000/api/test/
> 

Como dije anteriormente, usted deberá usar esta información para poder acceder a la información que le suministrará la API. 

Agregué en el encabezado de la petición las llaves "USERNAME" y "TOKEN" para generar una autenticación basica (Basic Auth). Y si realizó bien el proceso, la api le deberá generar una respuesta similar a la siguiente: 

![](https://i.ibb.co/3h5yzpF/sx3.jpg)

Y listo, ya está corriendo el servicio y la API. Recuerde que la lógica que se está usando para desencriptar la tarjeta por el archivo "keylog.txt", se encuentra de la carpeta restapidjango>readcard_class.py. En esta clase se compone de los métodos que permiten identificar el orden de los números, que se guía por dos vías:

- La primera es identificando el número que no tiene ningún otro antes del mismo
- La segunda es identificando el número que no tiene ningúnt otro después del mismo

Los une en unos arreglos y luego los compara. 

Las funciones necesarias se encuentran en el modulo readcard_functions.py de la misma carpeta. 