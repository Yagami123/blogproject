import multiprocessing

#bind = '67.209.185.139'
bind = 'unix:///tmp/www.light0lin.top.sock'
workers = multiprocessing.cpu_count()*2+1
reload = True
daemon = True
