FROM python:3.12

RUN apt update
# Node.js と npm のインストール
RUN apt install -y nodejs npm

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
