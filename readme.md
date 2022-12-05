# Flashcards.app

Flashcards application is built for learning English vocabulary for Poles.
By application, users can choose between 4 options(3 random translated word and 1 correct translated word),
then application check your option with main transaltion.
Application can give you some points for fastibility and good choice.
It is possible to set vocabulary repetitions for the user.
Users can show up your statistics about knows vocabulary.

## API endpoints

| Method   | URL                    | Description                       |
| -------- | ---------------------- | --------------------------------- |
| `POST`   | `/auth-token/`         | Retrive user auth token           |
| `GET`    | `/word`                | Show up all words.                |
| `POST`   | `/word`                | Create new word                   |
| `GET`    | `/word/<int:pk>`       | Retrive word with specific id     |
| `PUT`    | `/word/<int:pk>`       | Update word with specific id      |
| `DELETE` | `/word/<int:pk>`       | Delete word with specific id      |
| `GET`    | `/category`            | Show up all categorys.            |
| `POST`   | `/category`            | Create new category               |
| `GET`    | `/category/<int:pk>`   | Retrive category with specific id |
| `PUT`    | `/category/<int:pk>`   | Update category with specific id  |
| `DELETE` | `/category/<int:pk>`   | Delete category with specific id  |
| `GET`    | `/user`                | Show up all users.                |
| `POST`   | `/user`                | Create new user                   |
| `GET`    | `/user/<str:username>` | Retrive user with specific id     |

## Planowane funkcje

- generowanie losowe słowa
- generwoanie 3 losowych tlumaczen oraz 1 poprawnego
- sprawdzanie poprawnosci wyboru z tlumaczeniem głownego slowa
- naliczanie punktów - zaleznie od dokonanego wyboru
- ranking punktów

## Tech Stack

**Backend:** Django, Django Rest Framework
**SQL:** PostgreSQL

### Demo

Admin:

**Login -** admin
**Password -** admin

User:

**Login -** test_user
**Password -** test_user
