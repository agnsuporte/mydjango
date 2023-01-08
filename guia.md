# Ambiente Virtual:
01. ~ python3 -m venv venv
02. ~ source venv/bin/activate

# Install Django
03. ~ pip install django

# Start Project
04. ~ django-admin startproject <name-project> . 

# New Secret Key (its dont required)
05. ~ python manage.py shell
06. ~ from django.core.management.utils iport get_random_secret_key
07. ~ print(get_random_secret_key())

# Configuring Environment Variables
08. ~ pip install python-dotenv

    [In base.py (settings)]
    * from dotenv import load_dotenv
    * import os

    * load_dotenv()

    [Exemplo]
    * os.environ.get('SECRET_KEY')
