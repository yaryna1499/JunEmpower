#!/bin/bash

# Зупиняємо всі контейнери
docker stop $(docker ps -a -q)

# Видаляємо всі зупинені контейнери
docker rm $(docker ps -a -q)

# Видаляємо всі образи
docker rmi $(docker images -q)

# Видаляємо залишкові мережі
docker network prune -f 

# Видаляємо невикористовувані томи
docker volume prune -f

# Видаляємо cache builder'а
docker builder prune -f 

# Видаляємо залишкові файли системи docker
sudo rm -rf /var/lib/docker/tmp/* /var/lib/docker/cache/*

# Очищаємо журнали docker
sudo journalctl --vacuum-time=2weeks

echo "Очищення Docker системи завершено"
