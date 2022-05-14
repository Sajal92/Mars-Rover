FROM python:3.7.4-alpine3.10

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python","app.py"]