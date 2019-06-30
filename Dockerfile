FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY mutex/uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY mutex/app.conf /etc/nginx/conf.d/app.conf

ENV NGINX_WORKER_PROCESSES auto
ENV UWSGI_CHEAPER 0
ENV UWSGI_PROCESSES 1

ENV LISTEN_PORT "80"
EXPOSE 80

COPY mutex/requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY mutex/main.py /app/
