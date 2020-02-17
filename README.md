# hcmfront
apps SistemaTurnos (Python & Django REST)

se puede abrir el repositorio en gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/fbadilla/hcmfront)

por razones de accesibilidad, no fue incluido en el arcivho gitignore la base de datos (*.sqlite3), 
asi se podran realizar las pruebas y visualizar la informacion de forma inmediata

para correr el proyecto debe seguir los siguientes pasos
1) iniciar entorno virtual  
$ pipenv shell  
2) instalar dependencias  
$ pipenv install  
3) cambiar a la carpeta del proyecto  
$ cd Turnos  
4) creamos nuevas migraciones  
$ python manage.py makemigrations  
5) corremos las migraciones  
$ python manage.py makemigrations  
5) crear super usuario*** (usuario creado en BBDD cargada[user: admin, password: administrador]  
$ python manage.py createsuperuser  

URL
Usando la URLconf definida en turnos.urls, Django probó estos patrones de URL, en este orden:


admin /  
admin / ^ sistematurnos / turno /  
admin / ^ sistematurnos / dia /  
sistematurnos / ^ nuevo / [name = 'Turno_crear']  
sistematurnos / ^ listar [name = 'Turno_listar']  
sistematurnos / ^ eliminar / (<pk> ) / $ [name = 'Turno_eliminar']  
sistematurnos / ^ editar / (<pk> ) / $ [name = 'Turno_editar']  
sistematurnos / ^ mostrar / ( <pk> ) / $ [name = 'Turno_mostrar']  

print listado de turnos

![print lista](http://imgfz.com/i/n7hvdmE.png)

