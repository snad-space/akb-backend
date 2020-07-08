FROM python:3

EXPOSE 80

RUN pip install gunicorn psycopg2-binary

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["sh", "-c", "/app/docker-entrypoint.sh"]
