FROM python:3.6-alpine

WORKDIR /code

ADD . /code

RUN pip install -r requirements.txt --user

CMD ["python", "api.py"]
# ENTRYPOINT gunicorn --workers=4 --bind=0.0.0.0:5000 --access-logfile=- api:app
