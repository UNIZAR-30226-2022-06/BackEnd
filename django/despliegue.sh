heroku login #solo una vez
git init #solo una vez, para crear un repositorio
heroku git:remote -a db-itreader-unizar
git add .
git commit -m "mensaje"
git push heroku master

git push -f heroku
