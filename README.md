# async-django

Using Django Q for asynchronous tasks in your Django Application - Basic

# Setup 

1. Clone this repo
        
3. Get free heroku redis addon

        heroku login
        heroku create --addons=heroku-redis
        heroku config:get REDIS_URL
        
        Now you will get a REDIS_URL
        
4. Pass REDIS_URL as environment variable

        export REDIS_URL='redis://your_redis_url
        
5. Install Django Q and redis

        pip install django-q redis

6. Modify Django Q configuration in settings.py file

         Q_CLUSTER = {
            'name': 'your_project_name',
            'workers': 8,
            'recycle': 500,
            'timeout': 60,
            'compress': True,
            'save_limit': 250,
            'queue_limit': 500,
            'cpu_affinity': 1,
            'label': 'Django Q',
            'redis': os.environ.get('REDIS_URL')
          }
          
7. Run servers           

        python manage.py migrate
      
        python manage.py qcluster

8. Notice the logs and you can see the server returns response without any delay.

9. Redis database which is used as cache, holds all the tasks in a queue and then executes it.
        
        