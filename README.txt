step1:
pip install django
django-admin startproject assing
docker-compose run --rm app django-admin startproject doct


step2:
docker build -t doct . (doct is project name)
docker-compose build
docker-compose up
docker-compose up -d
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py runserver

docker-compose up --force-recreate -d


docker-compose run web python manage.py shell  

docker exec -it django_app /bin/bash