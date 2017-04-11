#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY zookeeper-3.4.9.tar.gz /root/pkg/
COPY jdk-7u79-linux-x64.tar.gz /root/pkg/
COPY start.sh /root/pkg/

RUN \
	mkdir /usr/local/zookeeper &&\
	mkdir /opt/java &&\
	tar -zxvf ~/pkg/zookeeper-3.4.9.tar.gz -C /usr/local/zookeeper --strip-components 1 &&\
	tar -zxvf ~/pkg/jdk-7u79-linux-x64.tar.gz -C /opt/java --strip-components 1 &&\
	cp /usr/local/zookeeper/conf/zoo_sample.cfg /usr/local/zookeeper/conf/zoo.cfg

#set path
ENV JAVA_HOME /opt/java
ENV JRE_HOME JRE_HOME=${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#port
EXPOSE 2181

#start cmd
#CMD [ "/usr/local/zookeeper/bin/zkServer.sh","start" ]
