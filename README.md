# Ingaia App

Ingaia App is an REST API that suggests a musical playlist according to the current temperature in the city previously informed. This project is available on heroku through the endpoints:
- [https://ingaia-app.herokuapp.com/docs](https://ingaia-app.herokuapp.com/docs) for Swagger documentation
- [https://ingaia-app.herokuapp.com/api/musical_weather/](https://ingaia-app.herokuapp.com/api/musical_weather/) for playlist suggestion
- [https://ingaia-app.herokuapp.com/api/searched_cities/](https://ingaia-app.herokuapp.com/api/searched_cities/) for all searched cities

# Temperature Ranges
  - Below 10ºC suggests Classical Music
  - Between 10ºC and 25ºC suggests Rock Music.
  - Above 26ºC suggests Pop Music.

# Technologies
  - Python 3.7 with FastAPI Framework
  - Docker
  - SqlAlchemy to database access and ORM pattern.
  - Postgresql as a database.
  - Pytest
  - Spotipy (Python library to Spotify API)
  - OpenWeather API

# How to Run
  To generate the OpenWeather and Spotify API keys go to [https://openweathermap.org/api](https://openweathermap.org/api) and [https://developer.spotify.com/](https://developer.spotify.com/)
  - First open the **docker-compose** and change the value of the environment variables in the path **services > ingaia > environment**
  - Run the `docker-compose up --build -d ingaia` command on your terminal
  - The container will go up in `localhost:80`
  - Open `http://localhost:80/docs` to access the swagger documentation
  - If you prefer to use Postman, you can choose to make an HTTP GET request for `/api/musical_weather/?city={your_city_here}` to receive a suggested playlist or `/api/searched_cities` to receive all cities already consulted

# How To Run Tests
  - Run application
  - Set up project environment variables
  - Enter in `tests/functional_tests` folder
  - Run `pytest -s -v --disable-warnings` on your terminal.

# Architecture
 - Service Application layer: where the controllers were developed, it is responsible for receiving and forwarding requests
 - Domain Service layer: core of validations and business logic before persist on database.
 - Domain Model layer: responsible for describing all application models that will later be mapped to the database.
 - Infrastructure layer: can be divided in one more layer
    - Data layer: responsible persistence with the database, using SqlAlchemy as ORM
 - Tests layer: responsible for testing the application services and domain services.

![Architecture](https://miro.medium.com/max/732/1*P4zm6LF9l0nRmyN2iqjgHQ.png)