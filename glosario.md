# glosario de comandos

## docker 

```bash
#!/bin/sh
 
docker pull /imagen:etiqueta/
	#descarga la imagen selecionada
docker images 
	#muestra la imagenes descargadas
docker image rm *imagen:etiqueta
	#elimina las imagenes seleccionadas

docker create /image:etiqueta/
	#crea el contenedor con base a la imagen selecionada
    --name /nombre del contenedor/
	#le asigna el nombre al contenedo que se creara
    --network /nombre de la red/
	#asigna la red para comunicacion entre contenedores 
    -p /puerto del s.o/ : /puerto del contenedor/
	#mapea el puerto de sistema operativo anfitrion al del conternedor
    -v /carpeta del s.o/:/carpeta del  contenedor/
	#monta la carpeta de sistema operativo anfitrion al del conternedor
    -e* /variable con su valor/
	#asigna las variables de entorno
docker start /id o nombre del contenedor/
	#inicializa el contenedor
docker stop /id o nombre del contenedor/	
	#detiene el contenedor
docker log /id o nombre del contenedor/
	#muestra los logs del contenedor ejecutados 
    --follow
	#mantiene los logs en patalla

docker run /image:etiqueta/
	#crea e inicializa el contenedor con base a la imagen selecionada y si no encuentra la imagen la descarga (pull, create y start). en cada ejecucion de este comando se crea un nuevo contenedor
    --name /nombre del contenedor/
	#le asigna el nombre al contenedo que se creara
    --network /nombre de la red/
	#asigna la red para comunicacion entre contenedores 
    -p /puerto del s.o/ : /puerto del contenedor/
	#mapea el puerto de sistema operativo anfitrion al del conternedor
    -v /carpeta del s.o/:/carpeta del  contenedor/
	#monta la carpeta de sistema operativo anfitrion al del conternedor
    -e* /variable con su valor/
	#asigna las variables de entorno

docker rm /id o nombre del contenedor/
	#elimina el contenedor indicado
docker ps
	#muestra los contenedores corriendo
    -a
	#muestra los contenedores creados

docker build /directorio o archivo/
	#construye una imagen de docker a partir de un archivo Dockerfile 
	-t "nombre de la nueva imagen"

```
