# DjangoTutorial
This is a django tutorial


# Create a virtual environment
python -m venv venv_name

Use one for each django project


# Activate virtual environment 
venv_name\Scripts\activate


# Install django with venv activated
python -m pip install django 


# Create a new project inside the venv folder
python -m django startproject project_name



# Run the server
python manage.py runserver



# Project vs App
App - web application that does somehting (ex: blog,..)
Project - Collection of apps for a website
A project can contain multiple apps
An app can be in multiple projects



# Create an app inside the project
python manage.py startapp portfolio



# Add portfolio to installed apps
tutorial/settings.py

'portfolio'


# Add views for portfolio
portfolio/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the portfolio index page")

To access it in browser we have to define an url for this in portfolio/urls.py



# Define the urls for portfolio
portfolio/urls.py

from django.views import path
from . import views

create the list urlpatterns

urlpatterns = [

]


# Include portfolio urls in the global project
tutorial/urls.py

from django.urls import, include

include the portfolio urls to the global project 
path("portfolio/", include("portfolio.urls"))


# Migrate
python manage.py migrate

This is to apply changes to the database

This looks at INSTALLED_APPS and creates any database tables or make any changes according to the database settings in tutorial/settings.py



# Create database models
This the way to define the database layout
Each model is represented by a class



# Make migrations
python manage.py makemigrations

To reate migrations for those changes
Do this when changing models.py
The structure of the database is availlable in portfolio/migrations/



# Use python shell
python manage.py shell



# Create admin user
python manage.py createsuperuser

define username, email and password to log into admin account

# Register question in the admin panel
portfolio/admin.py

from .models import Question
admin.site.register(Question)

This way the question will be displayed in the admin panel and can be managed from there.