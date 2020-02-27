# async-django

Using Django Q for asynchronous tasks in your Django Application - Basic

# Setup 

1. Clone this repo

2. Create Virtual Environment and install requirements

        pip install virtualenv
        virtualenv venv
        source venv/bin/activate
        pip intall -r requirements.txt
        
3. Login to heroku and get free heroku redis addon

        heroku login
        heroku create --addons=heroku-redis
        heroku config:get REDIS_URL
        
        Now you will get a REDIS_URL
        
4. Pass REDIS_URL as environment variable

        export REDIS_URL='redis://your_redis_url
        

5. Modify Django Q configuration in settings.py file if required

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
          
6. Run servers           

        python manage.py migrate
      
        python manage.py qcluster

7. Notice the logs in both the servers and you will find the tasks getting executed asynchronously.

8. Redis database which is used as cache, holds all the tasks in a queue and then executes it.
        
        