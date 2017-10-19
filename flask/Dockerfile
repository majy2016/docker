FROM ubuntu
RUN apt-get update && apt-get install -y python3-dev python3-pip python3-virtualenv nginx
RUN pip3 install gunicorn
RUN pip3 install flask
RUN pip3 install flask_sqlalchemy
RUN pip3 install requests
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /usr/local/pypj

EXPOSE 80

USER root


