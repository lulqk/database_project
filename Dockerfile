FROM python:3.8
LABEL "mainteiner"="Mateusz Grulkowski"
ENV PYTHONUNBUFFERED 1

RUN mkdir /bazy_danych
WORKDIR /bazy_danych
COPY requirements.txt /bazy_danych/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /bazy_danych/

RUN adduser user
USER user