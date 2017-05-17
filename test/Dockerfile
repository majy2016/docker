#Vsersion 0.1

#base image
FROM openjdk:8-jdk

#au
MAINTAINER majy<majiayang@zuozh.com>


COPY test.jar /root/pkg/
COPY apache-maven-3.3.9-bin.tar.gz /root/pkg/
COPY settings.xml /root/pkg/

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /opt/maven
RUN tar -zxvf ~/pkg/apache-maven-3.3.9-bin.tar.gz -C /opt/maven --strip-components 1
RUN rm -rf /opt/maven/conf/settings.xml
RUN cp ~/pkg/settings.xml /opt/maven/conf/

ENV MAVEN_HOME /opt/maven
ENV PATH ${MAVEN_HOME}/bin:$PATH

#port
EXPOSE 8081

#start cmd
#CMD ["/usr/local/tomcat/bin/catalina.sh",'run']

