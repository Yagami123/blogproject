## nginx and uwsgi configuration
refer to 
1. https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
2. https://gist.github.com/evildmp/3094281

## django 执行流程
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py sqlmigrate blog 0001 # 迁移数据库
4. 