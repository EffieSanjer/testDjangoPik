FROM python:3.10.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]

