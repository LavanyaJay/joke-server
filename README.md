## Table of content

- [Aim](#Goal)

- [How to start](#How-to-start)
- [Technologies used for this project](#Technologies-used-for-this-project)
- [Contributors](#Contributors)

## Goal

The goal of the project is to display programming jokes.

## How to start

In order to run this App follow the following steps;

1. Set up a Postgres database with docker running on port 5430 using password secret:
   `$ docker run -p 5430:5432 --name jokes-server -e POSTGRES_PASSWORD=secret -d postgres`

2. Clone the repository using the command `git clone https://github.com/LavanyaJay/joke-server`

3. Install python3 and pip3 as per your OS and then create and start a virtual environment:
   `sudo -H pip3 install -U pipenv`
   `pipenv install django`
   `pipenv shell`

4. Install the project dependencies:
   `pip3 install requirements.txt`

5. Run `python manage.py migrate`

6. Create admin account using `python3 manage.py createsuperuser`

7. Run `python3 manage.py makemigrations joke-server` to make migrations for the application.

8. Run `python manage.py migrate`

9. Start the development server using `python3 manage.py runserver`

10. Open localhost:8000 on your browser to view the app

## Models and Relations

The model used for the current project include;

- Joke

## Api Resources

User can test the following endpoints in the backend by making requests as shown:

- Fetches all jokes

* `http://127.0.0.1:8000/api/jokes/`

- Fetches a single joke by jokeId

* `http://127.0.0.1:8000/api/jokes/1`

## Technologies used for this project

- python3 django
- django-rest framework
- cors
- PostgreSQL

## Contributor

- Lavanya Jayapalan
