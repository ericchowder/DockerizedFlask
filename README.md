# Dockerized Flask + Vue Full Stack E2E app

The purpose of this app is to implement a simple full stack application with virtualization (containers) and CI/CD flow. This allows for focus on the DevOps portion (virtualization, CI/CD, testing) and removes worry about creating a complicated full stack application.

## Technologies

Here are the following technologies currently implemented:
- Frontend: Vue.js
- Backend: Flask
- Database: SqlAlchemy (sqlite)
- Virtualization: Docker
- Server: Heroku

Here are the technologies being looked into:
- Persistent DB: Docker Volumes, AWS
- CI/CD: Github Actions, Cirlce CI
- Testing: TasteCafé, Cypress
- Server Migration: Digital Ocean
- Mobile: Vue Native

## Flow

Sqlaclchemy -> Flask <-> Vue ==> Docker -> Heroku.yml -> Heroku

## Setup

Clone repository:
```
git clone https://github.com/ericchowder/DockerizedFlask.git
```

### Flask

Open a shell instance, cd into backend, create a .venv folder, create a virtualenv with 'pipenv shell', install dependencies, run app:
```
cd backend
pipenv shell
pipenv install
python app.py
```

Check if app is running on the port shown.

### Vue.js

Open another shell instance, cd into frontend, install dependencies via npm, run serve script:
```
cd frontend
npm i
npm run serve
```

Check if app is running on the port shown.

### Docker

*This assumes that the images are not available, and they will be created via Dockerfile.*

Navigate to directory containing the Dockerfile. Run the following command to create the image:

```
docker build -t my-docker-image .
```

The -t flag indicates the tag/name used to name it, and the dot indicates current directory.

Next, you can run 'docker images' to view all your images. You should see the newly created image. Now, run the following command to run the image:

```
docker run -p <host-port>:<container-port> -d my-docker-image
```

The -p flag indicates the ports, and -d indicates detached mode.

Visit the port that you exposed for the container and you should be able to access it. Run 'docker ps' to view all running containers.

### Heroku

Heroku does not support docker-compose to run multiple docker containers, so heroku.yml was created in order to alleviate that. Heroku.yml simple builds the front and back end as two separate containers, simply requires a deploy to heroku with the following command:

```
git push heroku master
```