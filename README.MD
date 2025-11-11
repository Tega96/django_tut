How i started the Django project.
1. installed python3
2. install pipevn file using the command   `pip install pipenv`.
3. install django app using `pipenv install django` : Here, pipenv creates a directory and install the necessary dependencies. 
4. run the `pipenv shell` to activate the virtual environment. This command installs the interpreter we use in Django. 
5. running `django-admin` will start a new project. It will also display all the commands you need to work with django.
The command `django-admin start project storefront .` opens a create a new directory called storefront in our current folder.
6. `python manage.py runserver` executes the application on a default server: 8000. You can explicitly state the port by mentioning it at the end of the command. 'pytho manage.py runserver 5000`
