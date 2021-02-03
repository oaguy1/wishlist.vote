FROM ubuntu:20.04

RUN apt update -y && apt upgrade -y

RUN apt install python3 python3-pip -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
