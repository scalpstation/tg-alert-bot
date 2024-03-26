FROM python:3.11-alpine

ENV PIPENV_VENV_IN_PROJECT=1

RUN mkdir /data

WORKDIR /data

COPY Pipfile* /data/

RUN pip install --upgrade pip && pip install pipenv && pipenv sync --dev

COPY . /data

ENTRYPOINT ["pipenv", "run", "python", "main.py"]
