#!/bin/bash
######################################################################
# @author      : grupo 6
# @file        : despliegue.sh
# @created     : lunes abril 4, 2021 19:19:01 CET
#
# @description : Despliegue de repositorio git en heroku
######################################################################
#Actualizar librerías necesarias para heroku
pip freeze > requirements.txt
#Actualizar repositorio git
git add .
echo "Añade un comentario al git commit: "
read comentario
git commit -m "$comentario"
#Actualizar commit en heroku
heroku maintenance:on
git push -f heroku
heroku maintenance:off
#Visualizar aplicación desplegada
heroku open

#ver log del servidor en producción
#heroku logs --tail --app rocky-waters-55301
#Probar despliegue en local
#heroku local
#Dejar de dar servicio
#heroku ps:scale web=0