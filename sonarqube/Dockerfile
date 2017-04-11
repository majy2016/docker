#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY jdk-8u91-linux-x64.tar.gz /root/pkg/
COPY sonarqube-5.6.6.zip /root/pkg/
COPY start.sh /root/pkg/
COPY sonar.properties /root/pkg/
COPY wrapper.conf /root/pkg/

RUN \
#	yum -y update && \
	yum -y install net-tools openssh-server unzip

RUN mkdir /opt/java

RUN \
	tar -zxvf ~/pkg/jdk-8u91-linux-x64.tar.gz -C /opt/java --strip-components 1 && \
	unzip ~/pkg/sonarqube-5.6.6.zip -d /usr/local/  && \
	rm -rf /usr/local/sonarqube-5.6.6/conf/sonar.properties  && \
	rm -rf /usr/local/sonarqube-5.6.6/conf/wrapper.conf && \
	mv ~/pkg/sonar.properties /usr/local/sonarqube-5.6.6/conf/ && \
	mv ~/pkg/wrapper.conf /usr/local/sonarqube-5.6.6/conf/

#set path
ENV JAVA_HOME /opt/java
ENV JRE_HOME JRE_HOME=${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#port
#EXPOSE 8080

#start cmd
#CMD ["/usr/local/tomcat/bin/catalina.sh",'run']