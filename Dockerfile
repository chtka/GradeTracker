FROM python:3.6

ADD requirements.txt /etc/requirements.txt

RUN pip install -r /etc/requirements.txt

CMD ["/bin/bash -c 'cd gradetracker; python manage.py runserver'"]

