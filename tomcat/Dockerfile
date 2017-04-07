#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY jdk-7u79-linux-x64.tar.gz /root/pkg/
COPY apache-tomcat-7.0.75.tar.gz /root/pkg/

RUN \
#	yum -y update && \
	yum -y install net-tools openssh-server

RUN mkdir /opt/java
RUN mkdir /usr/local/tomcat

RUN \
	tar -zxvf ~/pkg/apache-tomcat-7.0.75.tar.gz -C /usr/local/tomcat --strip-components 1  && \
	tar -zxvf ~/pkg/jdk-7u79-linux-x64.tar.gz -C /opt/java --strip-components 1 && \
	rm -rf /usr/local/tomcat/webapps/* && \
	sed -i "22a export JAVA_HOME=/opt/java" /usr/local/tomcat/bin/setclasspath.sh && \
	sed -i "22a export JRE_HOME=/opt/java/jre" /usr/local/tomcat/bin/setclasspath.sh
#set path
ENV JAVA_HOME /opt/java
ENV JRE_HOME JRE_HOME=${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH

#port
#EXPOSE 8080

#start cmd
#CMD ["/usr/local/tomcat/bin/catalina.sh",'run']