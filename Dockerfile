FROM python:3.6

ADD requirements.txt /etc/requirements.txt

RUN pip install -r /etc/requirements.txt

VOLUME [ "/src" ]

WORKDIR /src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

