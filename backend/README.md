# Backend

The backend of the application is written in Python and utilizes the [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) libraries. While it is possible to run this code locally, a Dockerfile is provided to ease development/deployment.

## Using manage.py

Assuming you are using the provided Dockerfile and docker-compose, running the manage.py for the project can be done using the command below (with your own arguments following after the ellipsis):

```bash
docker-compose run api manage.py ...
```