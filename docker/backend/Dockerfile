FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.7 python3.7-dev  && \
    apt-get -y install python3-pip
    #apt-get install sqlite3 libsqlite3-dev


WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.7 /usr/bin/python3
RUN pip3 install --upgrade pip
RUN pip3 install cython
RUN pip3 install numpy
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==19.9.0

ADD ./apps /app/apps
ADD ./docker /app/docker
ADD ./research /app/research
ADD ./mlappdeploy /app/mlappdeploy
ADD ./manage.py /app/


RUN mkdir -p app/staticfiles
RUN mkdir -p app/static
