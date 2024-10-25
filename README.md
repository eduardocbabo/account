Passo a passo nova instalação modulo account

python -m venv .venv
source .venv/bin/activate

pip install django
pip install django-unfold
pip install unfold
pip install django-extensions
pip install django-allauth


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
