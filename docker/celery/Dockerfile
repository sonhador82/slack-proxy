FROM python:3.5-alpine

RUN pip install flask gunicorn celery requests redis \
    && adduser -h /app -D celery

USER celery
ADD app/ /app
WORKDIR /app
CMD celery -A tasks worker -c1 -l info
