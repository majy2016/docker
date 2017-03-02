#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY nginx-1.10.3.tar.gz /root/pkg/
COPY nginx.conf /root/pkg/
COPY start.sh /root/pkg/

RUN \
	yum -y install net-tools pcre-devel zlib-devel make gcc libc6-dev && \
	tar -zxvf ~/pkg/nginx-1.10.3.tar.gz -C /root/pkg/

WORKDIR /root/pkg/nginx-1.10.3

RUN \
	./configure && \
	make install  && \
	rm -rf /usr/local/nginx/conf/nginx.conf   && \
	cp /root/pkg/nginx.conf  /usr/local/nginx/conf/

#port

#start cmd
#CMD ["/usr/local/nginx/sbin/nginx"]