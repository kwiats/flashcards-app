# Flashcards.app

The application is a dictionary quiz that displays an English word and four of its translations in Polish. The user must select the correct translation and receive points for it. The application can offer different levels of difficulty and categories of words, such as animal names, everyday objects, sports, etc. The user can also collect points and achieve higher levels, adding challenge and motivation to learn new words. This application may be useful for people learning English or wanting to improve their skills.

## API endpoints

| Method   | URL                                     | Description                                      |
| -------- | --------------------------------------- | ------------------------------------------------ |
| `POST`   | `/auth-token/`                          | Retrive user auth token                          |
| `GET`    | `/word/`                                | Show up all words.                               |
| `POST`   | `/word/`                                | Create new word                                  |
| `GET`    | `/word/<int:pk>/`                       | Retrive word with specific id                    |
| `PUT`    | `/word/<int:pk>/`                       | Update word with specific id                     |
| `DELETE` | `/word/<int:pk>/`                       | Delete word with specific id                     |
| `GET`    | `/category/`                            | Show up all categorys.                           |
| `POST`   | `/category/`                            | Create new category                              |
| `GET`    | `/category/<int:pk>/`                   | Retrive category with specific id                |
| `PUT`    | `/category/<int:pk>/`                   | Update category with specific id                 |
| `DELETE` | `/category/<int:pk>/`                   | Delete category with specific id                 |
| `GET`    | `/user/`                                | Show up all users.                               |
| `POST`   | `/user/`                                | Create new user                                  |
| `GET`    | `/user/<str:username>/`                 | Retrive user with specific id                    |
| `PUT`    | `/user/<str:username>/`                 | Update user with specific id                     |
| `PATCH`  | `/user/<str:username>/`                 | Updated single elements in user                  |
| `DELETE` | `/user/<str:username>/`                 | Delete user with specific id                     |
| `GET`    | `/ranking/`                             | Retrive lastest ranking                          |
| `POST`   | `/ranking/`                             | Create new ranking                               |
| `POST`   | `/user/<str:username>/changeemail/`     | Change email for user from username(in progress) |
| `POST`   | `/user/<str:username>/change-password/` | Change password for user from username           |

## Tech Stack

**Frontend:** HTML, CSS
**Backend:** Django, Django Rest Framework
**SQL:** PostgreSQL

### Demo

Admin:

**Login -** admin
**Password -** admin

User:

**Login -** test_user
**Password -** test_user

### Roadmap - notion

[Link here!](https://cat-ghoul-4e1.notion.site/cd52bb7c4c4940cd986431ec0ef96d3c?v=666e1a7f9f91412894a9b2d9b247ffd8)
