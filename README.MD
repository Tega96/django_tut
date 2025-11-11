## How i started the Django project.
1. installed python3
2. install pipevn file using the command   `pip install pipenv`.
3. install django app using `pipenv install django` : Here, pipenv creates a directory and install the necessary dependencies. 
4. run the `pipenv shell` to activate the virtual environment. This command installs the interpreter we use in Django. 
5. running `django-admin` will start a new project. It will also display all the commands you need to work with django.
The command `django-admin start project storefront .` opens a create a new directory called storefront in our current folder.
6. `python manage.py runserver` executes the application on a default server: 8000. You can explicitly state the port by mentioning it at the end of the command. 'pytho manage.py runserver 5000`


## Using integrated terminal
1. find the path to virtual environment `pipevn --venv`. copy the path.
2. click ctrl + p, search interpreter path, then paste the code there. ...and append '/bin/python' at the end

## Creating django app
1. Use the command `python manage.py startapp playground`. This opens a new app in our directory. 
2. You can access the intstalled apps in the settings file of the django app. There you can add or subtract whatever files you added or deleted. Content of the new app (playground include files such as):
    - migrations folder: for generating database tables
    - admin.py: to define how the admin interface for the app will look like
    - apps.py:- where we configure the app ( Just like config in nodeJS).
    - models.py:= to describe models for the app. To pull up information from the database and presents to the user. 
    - test.py:- where we write our unit test
    - views.py:- like a request handler

3. register your new app in the list of "INSTALLED APPS" in the setting.py file.

## Writing Views.
A view function takes a request and returns a response: ie, a request handler. A simple view looks like this: 
    ```from django.shortcuts import render
    from django.http import HttpResponse

    def say_hello(request):
        return HttpResponse('Hello world')
    ```
    The code above imports the HttpResponse module to enable  communication over the internet, then use the instance of the HttpResponse to send "Hello world" message.

## Mapping urls to view
1. Create a new file in playground app called url.py: This file will contain our url informations
2. Write a URLConf code to do the following: (every app has it's own url configuration)
    - import django.urls from path
    - import views from the current directory
    - create a list of urlpatterns: urlpatterns contains a list of our path. the path is a fuction consisting of a route(string) and view(function that returns a url pattern object).
    ```from django.urls import path
    from . import views

    urlpatterns = [
        path('playground/home/', view.say_hello)
    ]
    ```
3. Export the URLConf into the main url configuration for this project. Do the following:
    - Go to urls.py in the main django project (storefront), and import include from django.url
    - Next, your newly created url to the list of urlpatterns
    ```from django.urls import include

    urlpatterns = [
        path('playground/', include('playground.urls'))
    ]
    ```
    By so doing, django knows that every request made to the playground should be handled by the above route. 
    - test the api by visiting the appropriate endpoint on your browser. 

## Using Templates 
1. create a new folder in the root project directory called template. 
2. In it, create a html file. write some content in it. 
3. Configure your URLConf in views to handle a reqest to print out the content of your template. 
    
## Debuging Django app
1. install Django debug tool bar: visit this page ![Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
    - Use this command `python -m pip install django-debug-toolbar` it install
    - Add it to the list of installed apps in the settings.py
    - add the url: import debug_toolbar_url from debug_toolbar.toolbar and add it to urlpatterns of the project's urls.py
    - add the middleware in the setting: Middleware are used to hook into the django's request-responce processing.
    - copy and paste the 



# Building a data model
Data models are used to store and retrieve data
1. Identify the entities according to the project requirements and create the relationships between them. 

Each app in the django project have it's own data model.
Each app should do one thing and do it well. 

## Create new apps for the data model
1. Use the command `python manage.py startapp store` and `python manage.py startapp tags` to create two apps: store and tags for the ecomerce app. 
2. Add the new apps to the list of installed apps in our settings.py file.
3. Create a Models 

## Creating data models
1. Access the newly created app: store, and go to the model.py file
2. Create a model class (The class in Django is defined in the model's module)
3. Within the class, defined the fields in the class, and choose the appropriate field types and their respective options eg: types = models.CharField(max_length=255)
    ```class Product(models.Model):
            title = models.CharField(max_length=255)
            description = models.TextField()
            price = models.DecimalField(max_digits=6, decimal_places=2)
            inventory = models.IntegerField() 
            last_update = models.DateTimeField(auto_now=True)