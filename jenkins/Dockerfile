#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

COPY jdk-7u79-linux-x64.tar.gz /root/pkg/
COPY apache-tomcat-7.0.75.tar.gz /root/pkg/
COPY apache-maven-3.3.9-bin.tar.gz /root/pkg/

RUN \
#	yum -y update && \
	yum -y install net-tools openssh-server git

RUN mkdir /opt/java
RUN mkdir /usr/local/tomcat
RUN mkdir /usr/local/maven
RUN mkdir /root/.ssh
RUN mkdir /root/.jenkins

RUN \
	tar -zxvf ~/pkg/apache-tomcat-7.0.75.tar.gz -C /usr/local/tomcat --strip-components 1  && \
	tar -zxvf ~/pkg/jdk-7u79-linux-x64.tar.gz -C /opt/java --strip-components 1 && \
	tar -zxvf ~/pkg/apache-maven-3.3.9-bin.tar.gz -C /usr/local/maven --strip-components 1 && \
	rm -rf /usr/local/tomcat/webapps/* && \
	sed -i "22a export JAVA_HOME=/opt/java" /usr/local/tomcat/bin/setclasspath.sh && \
	sed -i "22a export JRE_HOME=/opt/java/jre" /usr/local/tomcat/bin/setclasspath.sh && \
	git config --global user.name "majiayang" && \
	git config --global user.email majiayang@zuozh.com
#set path
ENV JAVA_HOME /opt/java
ENV MAVEN_HOME /usr/local/maven
ENV JRE_HOME JRE_HOME=${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH
ENV PATH ${MAVEN_HOME}/bin:$PATH

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#port
#EXPOSE 8080

#start cmd
#CMD ["/usr/local/tomcat/bin/catalina.sh",'run']