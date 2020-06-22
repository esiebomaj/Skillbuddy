web: gunicorn skillbuddy.wsgi --log-file -
beat: celery -A skillbuddy beat -l info & worker: celery -A skillbuddy worker -events -loglevel info & wait -n