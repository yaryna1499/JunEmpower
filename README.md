# JunEmpower

#### Як запустити сервер локально?<br>
1 - створити .env із вмістом .env.example але замінити 'рут' на root<br>
2 - <i>sudo docker-compose up --build</i> в папці проекту (там де manage.py)<br>
3 - сервер тепер nginx, тому тепер 1443 порт<br>
4 - якщо буде помилка типу <i>'permission denied'</i>, то надайте усі дозволи із папки проекту:<br>
<i>sudo chmod -R 0777 *</i> в папці проекту (там де manage.py)<br>
документація до ендпоінтів http://localhost:1443/redoc/
