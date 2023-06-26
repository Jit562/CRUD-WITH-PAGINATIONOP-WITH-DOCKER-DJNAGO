Docker Images:

Docker images are the building blocks of Docker containers. An image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and dependencies. Images are created using a declarative text file called a Dockerfile, which specifies the instructions to build the image. Images are stored in a registry, such as Docker Hub, from where they can be pulled and run on Docker hosts.

Docker Containers:

Docker containers are lightweight, isolated, and portable environments that are created from Docker images. A container is an instance of an image that can be executed and run as an isolated process on a host machine. Containers provide a consistent and reproducible environment, ensuring that applications run consistently across different environments. Each container runs in its own isolated user space but shares the host system's kernel. Containers are ephemeral and can be started, stopped, moved, and deleted with ease. They offer advantages such as easy deployment, scalability, and resource efficiency.

Docker Volumes:

Docker volumes are used to persist and share data between containers and the host machine. A volume is a directory or filesystem within a container that has its lifecycle independent of the container itself. It allows data to be stored separately from the container, making it persistent even if the container is stopped or deleted. Volumes enable data to be shared and accessed by multiple containers, facilitating data consistency and collaboration. Docker volumes can also be used to mount files or directories from the host system into the container, allowing data to be easily exchanged between the container and the host.


In summary, Docker images provide the blueprint for creating Docker containers, which are isolated runtime environments that can be easily deployed and managed. Docker volumes, on the other hand, enable persistent data storage and sharing between containers and the host machine. Together, Docker images, containers, and volumes form the basis of Docker's containerization technology, offering a scalable and portable approach to application deployment and management.


commands:- 

step1:
pip install django
django-admin startproject assing
docker-compose run --rm app django-admin startproject assing


step2:
docker build -t snipetss . (snipetss is project name)
docker-compose build
docker-compose up
docker-compose up -d
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py runserver

docker-compose up --force-recreate -d


docker-compose run web python manage.py shell  
docker exec -it django_app /bin/bash


step3:- (Create the image and container status remove stop)
docker info
docker run -it ubuntu /bin/bash (ubuntu is docker image )
cat /etc/os-release ( check the container name )
docker images
docker search iamgesname
docker pull imagename
service docker status
docker start containername
docker attach containername
docker ps -a
docker ps
docker stop containername
docker rm containername
docker commit conatianername imagename (create the image using container) 

step4- 
docker valume create valumename
docker valume rm valumename
docker valume prune