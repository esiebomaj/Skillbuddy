web: gunicorn skillbuddy.wsgi --log-file -
beat: celery -A skillbuddy beat worker: celery -A skillbuddy worker -events -loglevel info 