# Flashcards.app

The application is a dictionary quiz that displays an English word and four of its translations in Polish. The user must select the correct translation and receive points for it. The application can offer different levels of difficulty and categories of words, such as animal names, everyday objects, sports, etc. The user can also collect points and achieve higher levels, adding challenge and motivation to learn new words. This application may be useful for people learning English or wanting to improve their skills.

## Tech Stack

**Frontend:** HTML, CSS
**Backend:** Django, Django Rest Framework
**SQL:** PostgreSQL

## Instalations

### Running the project

Clone the repository (make sure you have git installed):

```
git clone https://github.com/kwiats/flashcards-app
cd flashcards-app
```

Install the dependencies (Poetry will create a virtual environment automatically for you)

```
poetry install --with dev
```

You can start application in two ways.

1.  Build images and start containers. No worries, first run will take a lot of time. Docker has to download a lot of data, but it will store it in a cache for later retrieval.

```
docker-compose up --build
```

If everything went smoothly without errors, the application should now be running.
You can access it at

```
http://127.0.0.1:8000/
```

If you see the 404 page, then everything is correct.

Consider creating a superuser to access the Django Admin panel

```
docker-compose run django python manage.py createsuperuser
```

or

2.  Use Poetry to start server with django

```
poetry run python manage.py runserver
```

and for creatin a superuser to acces the Django Admin panel

```
poetry run python manage.py createsuperuser
```

## API endpoints

| Method   | URL                               | Description                                      |
| -------- | --------------------------------- | ------------------------------------------------ |
| `POST`   | `/auth-token/`                    | Retrive user auth token                          |
| `GET`    | `/word/`                          | Show up all words.                               |
| `POST`   | `/word/`                          | Create new word                                  |
| `GET`    | `/word/<int:pk>/`                 | Retrive word with specific id                    |
| `PUT`    | `/word/<int:pk>/`                 | Update word with specific id                     |
| `DELETE` | `/word/<int:pk>/`                 | Delete word with specific id                     |
| `GET`    | `/category/`                      | Show up all categorys.                           |
| `POST`   | `/category/`                      | Create new category                              |
| `GET`    | `/category/<int:pk>/`             | Retrive category with specific id                |
| `PUT`    | `/category/<int:pk>/`             | Update category with specific id                 |
| `DELETE` | `/category/<int:pk>/`             | Delete category with specific id                 |
| `GET`    | `/user/`                          | Show up all users.                               |
| `POST`   | `/user/`                          | Create new user                                  |
| `GET`    | `/user/<int:pk>/`                 | Retrive user with specific id                    |
| `PUT`    | `/user/<int:pk>/`                 | Update user with specific id                     |
| `PATCH`  | `/user/<int:pk>/`                 | Updated single elements in user                  |
| `DELETE` | `/user/<int:pk>/`                 | Delete user with specific id                     |
| `GET`    | `/ranking/`                       | Retrive lastest ranking                          |
| `POST`   | `/ranking/`                       | Create new ranking                               |
| `POST`   | `/user/<int:pk>/changeemail/`     | Change email for user from username(in progress) |
| `POST`   | `/user/<int:pk>/change-password/` | Change password for user from username           |
| `GET`    | `/user/<int:pk>/score/`           | Show up user current and spend score             |
| `PUT`    | `/user/<int:pk>/add_score/`       | Update user current and spend score              |
