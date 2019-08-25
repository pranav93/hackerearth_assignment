This project is developed in python version 3.6.8

# How do I install this project?
* Run following command to perform fresh dev environment setup.

```bash
chmod +x create_dev_setup.sh
./create_dev_setup.sh
```
* Create a superuser with username `username` and email `username@email.com`
by running following command. We will use this user for logging into our api 
and perform the api calls
```bash
python manage.py createsuperuser --username username --email username@email.com
```
* Now login by using our previously created user. And obtain the token
    * Method: POST
    * API endpoint : http://127.0.0.1:8000/api/login/
    * Payload: {"username": "dummy", "password": "dummy"}
    * Response: {"token": "some-token"}

![Alt text](screenshots/login.png?raw=true "Login")

* Create a game by call
    * Method: POST
    * API endpoint: http://127.0.0.1:8000/api/games/
    * Payload: { "game": { "title": "LittleBigPlanet PS Vita", "platform": "PlayStation Vita",
            "score": 9, "genre": "Platformer", "editors_choice": true}}
    * Response: {"success": "Game 'LittleBigPlanet PS Vita' created successfully"}

![Alt text](screenshots/create_game.png?raw=true "Create Game")

* Update a game by call
    * Method: PUT
    * API endpoint: http://127.0.0.1:8000/api/games/1
    * Payload: { "editors_choice": false}}
    * Response: {"success": "Game 'LittleBigPlanet PS Vita' updated successfully"}

![Alt text](screenshots/update_game.png?raw=true "Update Game")

* Get a game by game_id by calling
    * Method: GET
    * API endpoint: http://127.0.0.1:8000/api/games/1
    * Response: {
    "game": {
        "title": "LittleBigPlanet PS Vita",
        "platform": "PlayStation Vita",
        "score": 9,
        "genre": "Platformer",
        "editors_choice": false,
        "game_id": 1
    }}
    
![Alt text](screenshots/get_by_id.png?raw=true "Get Game By Id")

* Delete a game by call
    * Method: DELETE
    * API endpoint: http://127.0.0.1:8000/api/games/1
    * Response: {"success": "Game 'LittleBigPlanet PS Vita' deleted successfully"}

![Alt text](screenshots/delete_game.png?raw=true "Delete Game")

* Game a game by query parameters
    * Method: GET
    * API endpoint: http://127.0.0.1:8000/api/games?title=The Walking Dead: The Game -- Episode 3: Long Road Ahead
    * Response: {
    "games": \[
        {
            "title": "The Walking Dead: The Game -- Episode 3: Long Road Ahead",
            "platform": "Macintosh",
            "score": 9.0,
            "genre": "Adventure",
            "editors_choice": true,
            "game_id": 30
        },
        {
            "title": "The Walking Dead: The Game -- Episode 3: Long Road Ahead",
            "platform": "Xbox 360",
            "score": 9.0,
            "genre": "Adventure",
            "editors_choice": true,
            "game_id": 37
        },
        {
            "title": "The Walking Dead: The Game -- Episode 3: Long Road Ahead",
            "platform": "PC",
            "score": 9.0,
            "genre": "Adventure",
            "editors_choice": true,
            "game_id": 38
        },
        {
            "title": "The Walking Dead: The Game -- Episode 3: Long Road Ahead",
            "platform": "PlayStation 3",
            "score": 9.0,
            "genre": "Adventure",
            "editors_choice": true,
            "game_id": 39
        }
    \]
}
    * In this case we have option to provide keys \['title', 'platform', 'genre'\]
    * If we do not provide the request parameters, the api will return all of the games

![Alt text](screenshots/query.png?raw=true "Get Game List")

# Creating dummy data
* To create dummy data run command,
```bash
export username="username"
export password="password"
python create_data/create_data.py
```
