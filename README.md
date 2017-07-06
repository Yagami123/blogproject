## nginx and uwsgi configuration
refer to 
1. https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
2. https://gist.github.com/evildmp/3094281

## django 执行流程
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py sqlmigrate blog 0001 # 迁移数据库
4. 同步数据库 syncdb
5. python manage.py runserver


## django admin
1. 创建账户：python manage.py createsuperuser
 
        已创建账号： username:Light, password:lxd123456
2.                                                      
     
    ```
    def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
    ```

## 创建评论应用
1. python manage.py startapp comments
2. 在settings.py中注册这个应用

## gunicorn启动
gunicorn blogproject.wsgi:application -b 67.209.185.139 --reload
gunicorn -c gunicorn/gunicorn-conf.py -D --error-logfile gunicorn/error.log blogproject.wsgi

## 激活虚拟环境virtualenv
1. windows: env\Scripts\activate
2. linux: source env/bin/activate
3. 写入requirements.txt : pip freeze > requirements.txt

# vpn启动
/root/ss_start.sh


## 使用的开源库
1. django_markdown : https://github.com/klen/django_markdown
2. 