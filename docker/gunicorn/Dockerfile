FROM python:3.5-alpine

RUN pip install flask gunicorn celery requests redis \
    && adduser -h /app -D gunicorn

USER gunicorn
ADD app/ /app
WORKDIR /app
CMD gunicorn --bind 0.0.0.0:8080 app:flask_app
