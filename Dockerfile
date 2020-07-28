FROM ubuntu:18.04

RUN apt-get --fix-missing update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update 

RUN add-apt-repository universe
RUN apt-get update

RUN apt-get install firefox xvfb -y
RUN apt-add-repository ppa:mozillateam/firefox-next
RUN apt install firefox xvfb -y
RUN apt-get update --fix-missing && apt-get -y install python3-pip

WORKDIR /app

COPY requirements.txt /app/.
RUN pip3 install -r /app/requirements.txt
COPY ./ /app/
ENV PYTHONIOENCODING UTF-8
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install python3-tk -y
RUN apt-get install vim -y
ENV  PATH=$PATH:/app/.
CMD ["python3", "-u", "supervisor_check.py"]
