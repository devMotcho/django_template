# Template for Django Projects

## What does this project do?

This project serves as a template for Django projects, providing the following tools:

- Bootstrap alerts connected to django.contrib.messages
- Personalized Navbar, Sidebar, and Footer
- Main.html imports Font Awesome, Chart Js, and Bootstrap 5
- Change Mode to Dark and Light
- gitignore file
- Nice log in page

## How to use?

1. You need Python installed on your machine: [Python Downloads](https://www.python.org/downloads/)
2. Clone this repo:
   ```
   git clone <repo_url>
   ```
3. Navigate into the folder you just cloned
   ```
   cd <cloned_folder>
   ```
4. Create a virtual environment and install the dependencies:
   ```
   py -m venv venv
   pip install -r requirements.txt
   ```
5. Now you can make migrations, migrate, and run the server!
   ```
   py manage.py makemigrations
   py manage.py migrate
   py manage.py runserver
   ```
6. Create a superuser
   ```
   py manage.py createsuperuser --username=example --email=123@example.com
   ```
7. Or make a new app
   ```
   py manage.py startapp <app_name>
   ```
8. Have Fun!

# django_template
