#!/bin/bash

# Перевіряємо, чи запущено скрипт з правами суперкористувача (root).
if [[ $(id -u) -ne 0 ]]; then
  echo "Цей скрипт має бути запущений з правами суперкористувача (root)."
  exit 1
fi

# Оновлюємо списки пакетів перед установкою.
apt update

# Встановлюємо MySQL Server та MySQL Client.
apt install -y mysql-server mysql-client

# Перевіряємо, чи успішно пройшла установка.
if [[ $? -eq 0 ]]; then
  echo "Установка MySQL Server та MySQL Client успішно завершена."
else
  echo "Сталася помилка під час установки MySQL Server та MySQL Client."
fi

