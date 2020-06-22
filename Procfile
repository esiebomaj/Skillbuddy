web: gunicorn skillbuddy.wsgi --log-file -
worker: celery -A skillbuddy worker -events -loglevel info 
