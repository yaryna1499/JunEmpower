# JunEmpower

* [Trello link](https://trello.com/invite/b/POfUlFfE/ATTId5fe0550f25f46f2da9472abae9a17b94944872B/sprint-board)

#### Run project with nginx<br>
    ```sh
    cp .env.example .env
    source venv/bin/activate
    ```
    ```sh
    docker compose up
    ```

###### http://localhost:1443/redoc/<br>


#### Run project on gunicorn only<br>
    ```sh
    docker compose -f docker-compose-development.yaml up
    ```

(port 8000)<br>


#### Seed DB with fake data<br>
go to django shell
    ```sh
    docker compose exec app python3 manage.py shell
    ```
    ```sh
    >>>>> from seed_data import *
    >>>>> run_all()
    ```
