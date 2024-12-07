https://youtu.be/GE0Q8YNKNgs?si=ssY6trOh_7OQvg2r

pip freeze > requirements.txt

pip install -r requirements.txt


python -m virtualenv .venv

./.venv/Scripts/activate
.\.venv\Scripts\activate


pip install django

pip install djangorestframework


django-admin startproject drfsimplecrud .


python manage.py startapp projects

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
