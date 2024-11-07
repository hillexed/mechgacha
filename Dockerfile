FROM alpine:3.18.0
WORKDIR /root/

RUN ["apk", "--update-cache", "add", "python3", "python3-dev", "py3-pip", "gfortran", "musl-dev", "linux-headers", "g++"]

COPY mechgacha/requirements.txt /root/requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY mechgacha/ /root/mechgacha/

WORKDIR /root/mechgacha

CMD env > .env && python3 bot.py
