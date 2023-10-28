### Описание проекта 
foodgram - сервис для любителей котиков.

Что умеет проект:

- Добавлять, просматривать, редактировать и удалять котиков.
- Добавлять новые и присваивать уже существующие достижения. 
- Просматривать чужих котов и их достижения.

## Установка 

1. Клонируйте репозиторий на свой компьютер:

    ```bash
    git clone https://github.com/AlexAvdeev1986/foodgram_final.git
    ```
    ```bash
    cd foodgram_final
    ```
2. Создайте файл .env и заполните его своими данными. Перечень данных указан в корневой директории проекта в файле .env.example.
Fill it with your data

# Database Secrets
POSTGRES_USER=[database_username]
POSTGRES_PASSWORD=[database_password]
POSTGRES_DB=[database_name]
DB_PORT=[database_connection_port]
DB_HOST=[db]

# Django Secrets
SECRET_KEY='SECRET_KEY'
DEBUG=False
ALLOWED_HOSTS='your_domain'

### Создание Docker-образов
docker start db

1.  Замените username на ваш логин на DockerHub:

    ```bash
    cd backend
   docker build -t alex886/foodgram_backend:latest .
    cd frontend
   docker build -t alex886/foodgram_frontend:latest .
    cd gateway
   docker build -t alex886/foodgram_gateway:latest .
    ```

2. Загрузите образы на DockerHub:

    ```bash
    docker push alex886/foodgram_backend:latest
    docker push alex886/foodgram_frontend:latest
    docker push alex886/foodgram_gateway:latest
    ```
    sudo docker container ls

1. Подключитесь к удаленному серверу

    ```bash
   sudo ssh -i /home/alex/Загрузки/555/yc-ea703557 yc-user@158.160.8.70
key NRjeSf
 имя_пользователя@ip_адрес_сервера 
    ```

2. Создайте на сервере директорию foodgram через терминал

    ```bash
    mkdir foodgram
    ```

3. Установка docker compose на сервер:

    ```bash
    sudo apt update
    sudo apt --fix-broken install
    sudo apt install curl
    curl -fSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh
    sudo apt-get install docker-compose-plugin
    ```

4. В директорию foodgram/ скопируйте файлы docker-compose.production.yml и .env:

    ```bash
    scp -i path_to_SSH/SSH_name docker-compose.production.yml username@server_ip:/home/username/foodgram/docker-compose.production.yml
    * ath_to_SSH — путь к файлу с SSH-ключом;
    * SSH_name — имя файла с SSH-ключом (без расширения);
    * username — ваше имя пользователя на сервере;
    * server_ip — IP вашего сервера.g
    ```bash
   sudo ssh -i /home/alex/Загрузки/555/yc-ea703557 yc-user@158.160.8.70
key NRjeSf
 имя_пользователя@ip_адрес_сервера 
    ```

 scp -i /home/alex/Загрузки/555/yc-ea703557 docker-compose.production.yml  yc-user@158.160.8.70:/home/yc-user/foodgram/docker-compose.production.yml

 scp -i /home/alex/Загрузки/555/yc-ea703557 .env  yc-user@158.160.8.70:/home/yc-user/foodgram/.env
    ```

Далее выполняем последовательно на своем компьютере потом на сервере.
sudo docker compose -f docker-compose.production.yml pull
sudo docker compose -f docker-compose.production.yml down
sudo docker compose -f docker-compose.production.yml up -d
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collect_static/. /static_backend/static/

Создаем суперпользователся. Следуем инструкциям при выполнении.

sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser

запускаем 
docker compose up
sudo docker compose -f docker-compose.production.yml up

 docker run -e POSTGRES_PASSWORD=foodgram_password -e POSTGRES_USER=foodgram_user postgres:13

    ```

При пуше в ветку master на GitHub будет автоматически произведена сборка образов, пуш на DockerHub, развертывание и запуск контейнеров на сервере.

Дальше необходимо создать суперпользователя для развернутого проекта. Для этого в терминале подключиться к серверу и выполнить команду:

sudo docker exec -it <id контейнера с бэкендом> python manage.py createsuperuser
можно также выполнить загрузку ингредиентов в базу данных командой:

sudo docker exec -it <id контейнера с бэкендом> python manage.py load_data


Certbot - это инструмент, разработанный Let's Encrypt, который упрощает получение и установку SSL-сертификатов. Вы можете установить Certbot на своем сервере с помощью команды:
sql
Copy code
sudo apt update 
sudo apt-get install python3-certbot-nginx
sudo apt install certbot


7. На сервере в редакторе nano откройте конфиг Nginx:
```bash
    sudo ssh -i /home/alex/Загрузки/555/yc-ea703557 yc-user@158.160.8.70
key NRjeSf

...8Устанавливаем и настраиваем NGINX
Устанавливаем NGINX....

sudo apt install nginx -y
Запускаем
sudo systemctl start nginx
Настраиваем firewall
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
Включаем firewall
sudo ufw enable

...Открываем конфигурационный файл NGINX
sudo nano /etc/nginx/sites-enabled/default
Полностью удаляем из него все и пишем новые настройки...

1.Пример файла nginx находится в default



...Сохраняем изменения и выходим из редактора
Проверяем корректность настроек...
sudo nginx -t

Запускаем NGINX
sudo systemctl start nginx

Перезапускаем Nginx

sudo service nginx reload

Настраиваем HTTPS на сервере
Установка пакетного менеджера snap.
У этого пакетного менеджера есть нужный вам пакет — certbot.
Шаг 1. Установка certbot
Чтобы установить certbot, вам понадобится пакетный менеджер snap. Установите его командой:
sudo apt install snapd 
Далее сервер, скорее всего, попросит вам перезагрузить операционную систему. Сделайте это, а потом последовательно выполните команды:
# Установка и обновление зависимостей для пакетного менеджера snap.
sudo snap install core; sudo snap refresh core
# При успешной установке зависимостей в терминале выведется:
# core 16-2.58.2 from Canonical✓ installed 

# Установка пакета certbot.
sudo snap install --classic certbot
# При успешной установке пакета в терминале выведется:
# certbot 2.3.0 from Certbot Project (certbot-eff✓) installed

# Создание ссылки на certbot в системной директории,
# чтобы у пользователя с правами администратора был доступ к этому пакету.
sudo ln -s /snap/bin/certbot /usr/bin/certbot 
Шаг 2. Запускаем certbot и получаем SSL-сертификат
Чтобы начать процесс получения сертификата, введите команду:

sudo certbot --nginx 

Откройте файл sudo nano /etc/nginx/sites-enabled/default и убедитесь в этом:

Перезагрузите конфигурацию Nginx:
sudo systemctl reload nginx 


Чтобы узнать актуальный статус сертификата и сколько дней осталось до его перевыпуска, используйте команду:

sudo certbot certificates 

Теперь убедитесь, что сертификат будет обновляться автоматически: 
sudo certbot renew --dry-run 

Вручную сертификат можно обновить командой:
sudo certbot renew --pre-hook "service nginx stop" --post-hook "service nginx start" 



Запустите SSH-агент: Убедитесь, что SSH-агент запущен на вашем локальном компьютере и в него добавлен ваш приватный ключ с помощью ssh-add ...

chmod 600 yc-ea703557
ssh-add yc-ea703557

chmod 600 authorized_keys

eval "$(ssh-agent -s)"

ssh-add 

ssh-add ~/.ssh/authorized_keys 

полезное 

sudo apt upgrade

посмотреть все докер образы на сервере\



sudo docker images

sudo docker ps -a

sudo docker stop Image
sudo docker rm Image
sudo docker rmi Image Image


удалит все докер образы на сервере которые не используются
sudo docker system prune 

sudo docker rmi -f $(sudo docker images -q)


# /etc/nginx/sites-enabled/default
#Taski
server {

    root /var/www/html;
    index index.html index.htm;

    server_name alex86foodgram444.ddns.net;

    location / {
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/alex86foodgram444.ddns.net/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/alex86foodgram444.ddns.net/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot



}
server {
    if ($host = alex86foodgram444.ddns.net) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80 default_server;
    listen [::]:80 default_server;

    server_name alex86foodgram444.ddns.net;
    return 404; # managed by Certbot


}



#kittygram
#kittygram
server {
server_name alex86foodgram444.ddns.net;
server_tokens off;

location / {
    proxy_set_header Host $http_host;
    proxy_pass http://127.0.0.1:9000;


}

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/alex86foodgram444.ddns.net/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/alex86foodgram444.ddns.net/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot



}
server {
    if ($host = alex86foodgram444.ddns.net) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


listen 80;
server_name alex86foodgram444.ddns.net;
    return 404; # managed by Certbot


}

