## Запуск проекта
* Версия python 3.10.7 (На 3.8 тоже работает)
* Клонируем репозиторий себе в виртуальное окружение 

`git clone https://github.com/NiatpacBlack/flsk333.git`
* Переходим в папку проекта 

`cd flsk333`
* Устанавливаем зависимости из requirements.txt: 

`pip install -r requirements.txt`

* Для запуска приложения нужно подключить базу данных postgresql в файле config.py

[Подробнее по установке и настройке postgres в linux тут](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-ru)

Замените мою строку в файле на строку с вашими данными подключения к бд:

`SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://yourusername:yourpassword@localhost/your_db_name"`
* вводим команду: `flask run` для запуска приложения в тестовом режиме
### Развертывание проекта в локальной сети
* Для Unix-систем - установите gunicorn 

`pip install gunicorn`
* для запуска приложения вводим команду 

`gunicorn --bind 127.0.0.1:5000 wsgi:app`
### Настраиваем проксирование запросов с помощью nginx:
  * Устанавливаем nginx на вашу систему. Для ubuntu используем команду `sudo apt install nginx`
    
<details><summary>Если у вас не Ubuntu, а Manjaro как у меня. И при установке nginx нет нужных папок.</summary>
    
    `sudo pacman -S nginx`

   * Создаем каталоги:
  
    `sudo mkdir /etc/nginx/sites-enabled`

    `sudo mkdir /etc/nginx/sites-available`

    `sudo mkdir /etc/nginx/conf.d`
   * Правим конфиг, подключаем папку sites-enabled:
    
   `sudo nano /etc/nginx/nginx.conf`
    

   ```
    http {
        
        ##
        # Вставляем эти строчки в блок http в вашем конфиге
        ##
    
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        
    }
   ```

</details>
    
   * создаем файл с нашим конфигом для приложения 
    
   `sudo nano /etc/nginx/sites-available/flsk333.conf`

   ```
    server {
        listen 80;  
        
        access_log /var/log/nginx/flsk333.access.log;
        error_log /var/log/nginx/flsk333.error.log; 
        
        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }    
   ```

   * добавляем ссылку на наш конфиг в папку sites-enabled
    
   `sudo ln -s /etc/nginx/sites-available/flsk333.conf /etc/nginx/sites-enabled/`
   * перезапускам сервер

   `sudo systemctl restart nginx`

#### Можем проверять наш сайт по адресу 127.0.0.1 (По умолчанию nginx работает на 80 порту, можете изменить в конфиге на любой свободный порт.)
