# JunEmpower


#### Як запустити сервер локально?<br>
- <i>sudo docker-compose up --build</i> в папці проекту (там де manage.py)<br>
- сервер тепер nginx, тому тепер 1443 порт<br>
- не забудьте <i>cp .env.example .env</i><br>
###### документація до ендпоінтів http://localhost:1443/redoc/<br>
Trello - https://trello.com/invite/b/POfUlFfE/ATTId5fe0550f25f46f2da9472abae9a17b94944872B/sprint-board

#### Докер без nginx для локальної розробки<br>
<i>sudo docker compose -f docker-compose-development.yaml up --build</i><br>
port 8000
