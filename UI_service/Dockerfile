FROM python:3.12-slim

WORKDIR /app
COPY ./app /app

RUN pip install -r ./requirements.txt

EXPOSE 1338

CMD ["python3", "server.py"]
