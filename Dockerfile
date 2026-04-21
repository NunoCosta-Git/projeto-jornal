FROM python:3 as base 

WORKDIR /usr/src/app

COPY . .
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "jornal.wsgi"]