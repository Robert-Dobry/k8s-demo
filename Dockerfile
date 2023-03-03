FROM python:alpine

WORKDIR /app

ADD server.py /app

RUN pip install flask

CMD ["python3", "server.py"]

