pip install virtualenv
virtualenv venv       
.\venv\Scripts\activate
django-admin startproject UES
pip install django
django-admin startapp fisioterapias
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver