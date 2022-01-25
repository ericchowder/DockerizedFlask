# Dockerized Flask + Vue Full Stack E2E app

The purpose of this app is to implement a simple full stack application 
with virtualization (containers) and CI/CD flow. This allows for focus
on the DevOps portion (virtualization, CI/CD, testing) and removes worry
about creating a complicated full stack application.

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
>git clone https://github.com/ericchowder/DockerizedFlask.git

### Flask

Open a shell instance, cd into backend, create a .venv folder, create 
a virtualenv with 'pipenv shell', install dependencies, run app:
> cd backend
> pipenv shell
> pipenv install
> python app.py

Check if app is running on the port shown.

### Vue.js

Open another shell instance, cd into frontend, install dependencies via
npm, run serve script:
> cd frontend
> npm i
> npm run serve

Check if app is running on the port shown.

### Docker

*This assumes that the images are not available, and they will be created
via Dockerfile.*

