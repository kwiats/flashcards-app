# Flashcards.app

Flashcards application is built for learning English vocabulary for Poles.
By application, users can choose between 4 options(3 random translated word and 1 correct translated word),
then application check your option with main transaltion.
Application can give you some points for fastibility and good choice.
It is possible to set vocabulary repetitions for the user.
Users can show up your statistics about knows vocabulary.

# API endpoints

| Method   | URL                                      | Description                       |
| -------- | ---------------------------------------- | --------------------------------- |
| `GET`    | [`/auth-token/`](#get-token)             | Retrive user auth token           |
| `GET`    | [`/word`](#get-word)                     | Show up all words.                |
| `POST`   | [`/word`](#add-word)                     | Create new word                   |
| `GET`    | [`/word/<int:pk>`](#get-word)            | Retrive word with specific id     |
| `PUT`    | [`/word/<int:pk>`](#update-word)         | Update word with specific id      |
| `DELETE` | [`/word/<int:pk>`](#delete-word)         | Delete word with specific id      |
| `GET`    | [`/category`](#get-category)             | Show up all categorys.            |
| `POST`   | [`/category`](#add-category)             | Create new category               |
| `GET`    | [`/category/<int:pk>`](#get-category)    | Retrive category with specific id |
| `PUT`    | [`/category/<int:pk>`](#update-category) | Update category with specific id  |
| `DELETE` | [`/category/<int:pk>`](#delete-category) | Delete category with specific id  |
| `GET`    | [`/user`](#get-user)                     | Show up all users.                |
| `POST`   | [`/user`](#add-user)                     | Create new user                   |
| `GET`    | [`/user/<str:username>`](#get-user)      | Retrive user with specific id     |

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
