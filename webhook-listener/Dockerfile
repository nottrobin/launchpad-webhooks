FROM ubuntu

WORKDIR /srv
RUN mkdir events
RUN apt-get update && apt-get install --yes python3 less vim
COPY listener.wsgi.py .

ENTRYPOINT ["python3", "listener.wsgi.py"]
