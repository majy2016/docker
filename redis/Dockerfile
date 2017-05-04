#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY redis-3.2.8.tar.gz /root/pkg/

RUN \
	yum -y install make gcc libc6-dev
#	yum -y update && \

RUN \
	mkdir /usr/local/redis &&\
	tar -zxvf ~/pkg/redis-3.2.8.tar.gz -C /usr/local/redis --strip-components 1 &&\
	make MALLOC=libc -C /usr/local/redis/ &&\
	make MALLOC=libc -C /usr/local/redis/ install

RUN \
    sed -i "61s/bind 127.0.0.1/#bind 127.0.0.1/g" /usr/local/redis/redis.conf && \
    sed -i "80s/protected-mode yes/protected-mode no/g" /usr/local/redis/redis.conf

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#port
EXPOSE 6379

#start cmd
#CMD [ "redis-server --protected-mode no" ]
