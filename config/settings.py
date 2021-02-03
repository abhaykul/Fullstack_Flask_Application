DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com'
MAIL_PASSWORD = 'awesomepassword'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
result_backend = 'redis://:devpassword@redis:6379/0'
accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'
redis_max_connections = 5
