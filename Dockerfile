FROM django:onbuild

WORKDIR /usr/src

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

RUN python manage.py migrate

RUN python manage.py collectstatic

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
