## Решение Docker
### Первое задание:
<img width="1865" height="943" alt="изображение" src="https://github.com/user-attachments/assets/9b3a89d5-72cd-4d50-9d6a-73820d1bb3e1" />

Первая команда довольно простая, она запускает простой образ, который часто используют для проверки установлен ли Docker

### Второе задание:
<img width="1866" height="946" alt="изображение" src="https://github.com/user-attachments/assets/7359b73f-b872-4fbe-a7e9-79af3f2a7829" />

Вторая команда означает, что позволяет создать и запустить контейнер на основе официального Docker-образа

Треть команда Docker ps просто отображает список активных контейнеров в системе

### Третье задание:
<img width="1856" height="929" alt="изображение" src="https://github.com/user-attachments/assets/da83db61-4e78-486a-9dae-9c68d6e3ccac" />
Тут тестовое задание, выбрал Docker run -it ubuntu exit. Запускает контейнер в Ubuntu, а дальше команда exit - выводит из контейнера

### Четвертое задание:
<img width="1865" height="942" alt="изображение" src="https://github.com/user-attachments/assets/b9fc3586-7da3-4ae8-920f-b9cd69c093d7" />
docker run -d — name colleague_project my_project - запускает контейнер из образа my_project в фоне и присваивает ему имя colleague_project
docker ps — filter "name=colleague_project" - показывает запущенные контейнеры по фильтру названия
docker logs colleague_project - выводит логи контейнера

### Пятое задание:
<img width="1859" height="937" alt="изображение" src="https://github.com/user-attachments/assets/50c51b19-f645-4795-aabf-e213723b5975" />
docker stop colleague_project - Останавливает запущенный контейнер 
docker rm colleague_project - Удаляет остановленный контейнер

### Шестое задание:
<img width="1856" height="938" alt="изображение" src="https://github.com/user-attachments/assets/4e46780e-df06-4eeb-8551-2a5abe6acd55" />
docker pull hello-world - Скачивает или обновляет образ hello-world из Docker Hub

### Седьмое задание:
<img width="1859" height="929" alt="изображение" src="https://github.com/user-attachments/assets/016a7f99-4495-4566-b367-714aaec6ab81" />
docker images - покажет список всех локальных Docker-образов с их описанием
docker pull ubuntu:22.04 - команда скачивает образ ubuntu версии 22.04

### Восьмое задание:
<img width="1858" height="928" alt="изображение" src="https://github.com/user-attachments/assets/e42fd048-a30c-4118-884f-76ff0130ed22" />
docker rmi ubuntu - удаляет образ ubuntu
docker container prune - удаляет все остановленные контейнеры
docker image prune -a - удаляет все образы, которые в свою очередь не используются ни одним контейнером

## Docker intermediate
### Первое задание:
<img width="1855" height="933" alt="изображение" src="https://github.com/user-attachments/assets/a93663ff-5544-4965-91e0-0470821ec305" />
Задание тестовое и спрашивается какой команды нет в docker, 
docker trace - такая команда отсутсвует в документации
### Второе задание:
<img width="1857" height="928" alt="изображение" src="https://github.com/user-attachments/assets/102bb4e5-a883-49ca-8bb6-3746f63ab245" />
В следующем задании необходимо донаписать в файле с расширением sh, команду docker ps и запустить ее в терминале 
