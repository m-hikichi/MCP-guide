FROM python:3.12

RUN apt update
# Node.js と npm のインストール
RUN apt install -y nodejs npm
RUN npm install -g @modelcontextprotocol/inspector@0.13.0

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
