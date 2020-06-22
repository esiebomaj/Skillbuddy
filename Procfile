web: gunicorn skillbuddy.wsgi --log-file -
beat: celery -A skillbuddy beat -l info & celery -A skillbuddy worker -l info -P gevent & wait -n
