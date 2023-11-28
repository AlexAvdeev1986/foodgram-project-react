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

 python3 -m venv venv 
 
  source venv/bin/activate

  pip install django
  pip install djangorestframework


pip install python-decouple

pip install psycopg2-binary

python3 manage.py migrate


Загружаем на сервер

Правим на компе
chmod 600 /home/alex/Загрузки/555/yc-ea703557

scp -i /home/alex/Загрузки/555/yc-ea703557 docker-compose.production.yml  yc-user@158.160.8.70:/home/yc-user/foodgram/docker-compose.production.yml


scp -i /home/alex/Загрузки/555/yc-ea703557 docker-compose.yml  yc-user@158.160.8.70:/home/yc-user/foodgram/docker-compose.yml


scp -i /home/alex/Загрузки/555/yc-ea703557 .env  yc-user@158.160.8.70:/home/yc-user/foodgram/.env
  ```



sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser




запускаем
sudo docker compose up
sudo docker compose -f docker-compose.production.yml up
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate --noinput
sudo docker compose exec backend python manage.py createsuperuser
sudo docker compose exec backend python manage.py collectstatic --no-input
7. Для добавления ингредиентов в базу данных, выполните команду:
С проектом поставляются данные об ингредиентах.  
Заполнить базу данных ингредиентами можно выполнив следующую команду:
```bash
sudo docker compose exec backend python manage.py import_csv data/ingredients.csv

```

на сервере развернуть 
sudo docker compose -f docker-compose.production.yml up 

sudo docker compose -f docker-compose.production.yml up -d


docker run -e POSTGRES_PASSWORD=foodgram_password -e POSTGRES_USER=foodgram_user postgres:13



sudo ssh -i /home/alex/Загрузки/555/yc-ea703557 yc-user@158.160.8.70
key NRjeSf



sudo docker images
sudo docker ps -a




sudo docker stop Image
sudo docker rm Image
sudo docker rmi Image Image


остановить все контейнеры в докер
sudo docker stop $(sudo docker ps -aq)


удалить  все контейнеры в докер
sudo docker rm $(sudo docker ps -aq)


остановить все образы в докер
sudo docker stop $(sudo docker ps -aq)


удалить все образы
sudo docker rmi -f $(sudo docker images -q)




# Checking Docker version
docker --version

# Clean up resources from previous jobs
docker system prune -a

# Create local container network
docker network create my_network

# Starting Postgres service container
docker run -d --name postgres_container --network my_network -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:latest

# Waiting for all services to be ready
# You can add a sleep or use a tool like `wait-for-it.sh` to wait for the Postgres container to be ready before proceeding.

# Service container postgres failed.
# Check logs for the postgres_container to identify the issue
docker logs postgres_container

# Error: One or more containers failed to start.
# Investigate the logs and fix the issue before retrying the container startup.

удалит все докер образы на сервере которые не используются
sudo docker system prune
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
      proxy_pass http://127.0.0.1:9000;
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