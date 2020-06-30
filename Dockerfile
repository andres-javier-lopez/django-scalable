FROM python:3

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN pip install -e .

CMD ["python", "manage.py", "runserver", "0:8000"]
