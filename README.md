SOBRE EL PROYECTO:

Nuestro propósito es crear una plataforma para la organización Colunga y todas las demás organizaciones que participan en ella con el fin de crear un espacio donde se pueda desarrollar la comunidad virtual entre colaboradores y que estos puedan llevar a sus reuniones y mantenerse informados acerca de las actividades que se organicen de una manera óptima. 

  Construido con:
  
  -JQuery

  -Django
  
COMO EMPEZAR:

  Pre-requisitos: 

	- Python 3.7 o superior
	- pip de python 
  	- En caso de querer editar el proyecto, debe disponer de un entorno de desarrollo compatible con python


  Instalación para VER página web: 
  
  	! Si dispone de un dispositivo macOS debe remplazar los comandos "python" por "python3"
  
	1. Descargar ZIP del repositorio (https://github.com/Elsapallo/Plataforma-Colunga.git)
  	2. Dirigirse desde su consola (CMD) a la carpeta descargada y luego a Sprint1
 	 ej:
    		cd Downloads
    		cd Plataforma-Colunga-main
		cd Sprint1
		
	y escribir lo siguiente:

		python manage.py migrate
   
  para VER la página web: 
  	
  	3. Escribir en la consola:  python manage.py runserver
  	4. Abrir el navegador y buscar la url:  http://127.0.0.1:8000/
  
  Listo para ver página web:)
  
  para EDITAR página web: 
  
	3. Escribir en la consola:
	
  		python -m pip install Pillow 
		python -m pip install django-admin-interface
      		pip install -r requirements.txt
      
  listo para editar proyecto:)
  
  !IMPORTANTE
  
  Si usted va a administrar el sitio debe crearse una cuenta sigiendo los siguientes pasos: 
  
  1. Debe estar en la carpeta Sprint1
  2. Debe escribir en la consola lo siguinte:
      
      	-python manage.py createsuperuser

  3. ingrese su nombre,correo y cree su contraseña
  
  Usted está list@ para administrar el sitio:)

USO

1. vaya a su navegador y busque: http://127.0.0.1:8000/

1+. Si desea administrar el sitio, debe ingresar a su navegador la url:  http://127.0.0.1:8000/admin/ 

+ADMIN+
- Debe ingresar con el usuario creado en "!IMPORTANTE"
- Aquí usted podrá ingresar miembros, instituciones y otros administradores que podrán realizar acciones que usted decida que puede modificar
- Para ingresar miembros, debe haber creada una institución (porque usuario debe pertenecer a una)
! Al ingresar un miembro, el campo "PIN" no se debe modificar


VÍAS A MEJORAR (ver issues)

/////////////////


CONTRIBUCIÓNES

///////////


LICENCIA

 GNU public license v3


CONTACTO

f.cidgon@gmail.com

https://github.com/Elsapallo


RECONOCIMIENTO

- Font awesome

- Boostrap

- Html5up.net

- Scrollex (github.com/ajlkn/jquery.scrollex)

- Responsive Tools (github.com/ajlkn/responsive-tools)

- SCSS
