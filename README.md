
# JunEmpower

* [Trello link](https://trello.com/invite/b/POfUlFfE/ATTId5fe0550f25f46f2da9472abae9a17b94944872B/sprint-board)


## Run Locally

Create virtual environment

```bash
  python3 -m venv venv
```

```bash
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Copy environment variables

```bash
  cp .env.example .env
```
Start the db

```bash
  docker compose up db -d
```
Run migrations

```bash
  python3 manage.py migrate
```
Run server

```bash
  python3 manage.py runserver
```
Seed fake data in db

```bash
  python3 manage.py shell
```
```bash
  from seed_data import *
  run_all()
```
(make sure that POSTGRES_HOST=localhost)
### 

[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


## Common problems

Django don't serve staticfiles

```bash
  python3 manage.py collectstatic --no-input
```
Docker problems:
- busy ports by containers from another projects<br>
Stop all containers

```bash
  docker stop $(docker ps -a -q)
```
- permission denied for db folder<br>
Give recursive permission for all project files(bad practise, but ...)
```bash
  sudo chmod -R 0777 *
```

