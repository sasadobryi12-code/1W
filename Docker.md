## Накопленные баллы:

<img width="387" height="151" alt="изображение" src="https://github.com/user-attachments/assets/03373a63-3e6e-4cac-ae59-78eb25fbc244" />

По почте имя Саша, не обращайте на это внимания, это некий интернет псевдоним


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

### Третье задание:

<img width="1858" height="943" alt="изображение" src="https://github.com/user-attachments/assets/766da876-7043-4fda-90b5-94a866042735" />
В следующем задании тестовый вопрос.Необходимо было выбрать команду, которая используется для автоматической очистки контейнера, который запущен на Alpine Linux, когда он завершит работу: docker run -it --rm alpine:3.19.2

### Четвертое задание:

<img width="1860" height="935" alt="изображение" src="https://github.com/user-attachments/assets/8ab25f66-0caf-4337-abbd-ecf11ba288c0" />
В следующем задании Необходимо было запустить образ контейнера crane с помощью docker, после чего изменить файл ~/workspace/customerdata.json и обновить запись "Company Name" на The File Store. После чего запустить образ контейнера crane и передать файл ~/workspace/customerdata.json в путь /customerdata.json внутри контейнера. Запуск контейнера: docker run crane, в самом редакторе поменять название на The File Store, после чего запустить docker: docker run -v ~/workspace/customerdata.json:/customerdata.json, формат -v монтирует локальный файл внутрь контейнера, позволяя читать данные без пересборки

### Пятое задание:

<img width="1911" height="941" alt="изображение" src="https://github.com/user-attachments/assets/dcb44563-945c-48c2-9b62-d82367dd9a03" />
Простое тестовое задание

### Шестое задание:

<img width="1913" height="927" alt="изображение" src="https://github.com/user-attachments/assets/d62ae721-3372-4248-99b7-8f401d70e780" />

Для корректной передачи конфигурации важно соблюдать имя файла и путь внутриконтейнера, указанные в требованиях приложения

### Седьмое задание:

<img width="1913" height="934" alt="изображение" src="https://github.com/user-attachments/assets/ce732b19-c85a-48e5-9c46-4e4a5cc0a2a0" />

docker volume create validation_test - Создает управляемый Docker-том, который хранится в специальной директории на хосте и не зависит от жизненного циклв контейнера, docker volume ls - показывает списки всех созданных томом и docker run -v validation_test:/data ubuntu:24.04 - монтирует в указанный путь внутри контейнера. Данные, записанные в /data, будут сохранены в томе даже после остановки контейнера, что делает их персистентными

### Восьмое задание:

<img width="1915" height="934" alt="изображение" src="https://github.com/user-attachments/assets/d79d0758-2f59-43b5-b2bd-e16f68a80820" />

docker volume ls - Выведет список томов, docker run -v shared_data_volume:/data -it alpine:3.19.2 ls /data - Заменит shared_volume на реальное имя из тома 1 и после чего необходимо повторно запустить эту же команду


## containerization-and-virtualization-concepts

### Первое задание:

<img width="1919" height="938" alt="изображение" src="https://github.com/user-attachments/assets/0b3c7c83-ba9d-46f8-b5ca-9939d7d41010" />

Ключевыми ограничениями физических машин по сравнению с виртуальными или облачными решениями: Стоимость, Масштабируемость, Обслуживание

### Второе задание:

<img width="1911" height="934" alt="изображение" src="https://github.com/user-attachments/assets/20f908a0-a03c-4368-9630-ef9de883b174" />

Виртуальная машина это не физическое устройство, а программная эмуляция целой операционной системы с ее собственными ресурсами(CPU, RAM, диск), работающая поверх хостовой ОС или гипервизора. Это в свою очередь позволяет запускать несколько независимых компьютеров на одном физическом сервере 

### Третье задание:

<img width="1909" height="930" alt="изображение" src="https://github.com/user-attachments/assets/ecfcf47d-2e5e-45f3-8309-7a8da60697f2" />

