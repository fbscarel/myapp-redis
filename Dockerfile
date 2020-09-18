FROM python:3.6-alpine

WORKDIR /opt

COPY . /opt/

RUN pip install requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "app.py"]
