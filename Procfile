web: gunicorn skillbuddy.wsgi --log-file -
worker: celery -A skillbuddy worker -l info -P gevent
