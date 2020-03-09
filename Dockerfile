FROM python:slim-buster

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    jq \
    tzdata \
    gcc \
    g++ \
    ca-certificates \
    wget && \
    update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# INSTALL AWS DEPS
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

ADD Pipfile* ./

RUN pip install --no-cache -U pip pipenv && pipenv install --system


RUN apt-get remove --purge -y \
    tzdata \
    gcc \
    g++ \
    wget && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y

ADD . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "src.app:app", "-c ./src/gunicorn.py"]

