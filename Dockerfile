FROM python:3.11

RUN apt-get clean &&  apt-get update && apt-get -fy install ffmpeg
RUN pip install --upgrade pip

COPY ./requirements.txt /tmp/
WORKDIR /tmp/
RUN pip install -r requirements.txt

COPY . /usr/src/app/
WORKDIR /usr/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]