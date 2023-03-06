FROM python:alpine

WORKDIR /app

ADD /src/server.py /app

RUN pip install flask

CMD ["python3", "server.py"]

