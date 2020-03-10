FROM python:slim-buster

WORKDIR /srv

ADD Pipfile* ./

RUN pip install --no-cache -U pip pipenv && pipenv install --system

ADD . .

EXPOSE 80

ENTRYPOINT ["uvicorn", "--workers=1", "--host 0.0.0.0", "--port 80",  "src.app:app"]

