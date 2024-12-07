https://youtu.be/GE0Q8YNKNgs?si=ssY6trOh_7OQvg2r

pip freeze > requirements.txt

pip install -r requirements.txt


python -m virtualenv .venv

./.venv/Scripts/activate
.\.venv\Scripts\activate

pip install django

django-admin startproject server .

pip install djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
