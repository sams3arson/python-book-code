import gevent
from gevent import monkey
monkey.patch_all() # monkey-patching standard libs
import socket

hosts = ['www.google.com', 'www.apple.com',
         'www.archlinux.org']

jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)

# gevent.spawn() создает гринлет (greenlet), называемый также зеленым потоком или
# микропотоком; разница заключается в том, что зеленый поток не блокируется: если
# произошло какое-то событие, которое заблокировало поток, gevent переключит
# управление на другой зеленый поток
# geven.joinall() ожидает завершения всех созданных задач
# Доки: https://sdiehl.github.io/gevent-tutorial/

# tornado и gunicorn - два других популярных фреймворка, основанных на событиях
# помогают обрабатывать события на низком уровне и предоставляют быстрый веб-
# сервер

