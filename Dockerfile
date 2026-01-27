FROM python:3.13-bookworm

EXPOSE 80

RUN pip install gunicorn psycopg[binary]

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["sh", "-c", "/app/docker-entrypoint.sh"]
