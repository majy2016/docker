#Vsersion 0.1

#base image
FROM openjdk:8-jdk

#au
MAINTAINER majy<majiayang@zuozh.com>


COPY mock-oos.jar /root/pkg/

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#port
EXPOSE 8888

#start cmd
#CMD ["/usr/local/tomcat/bin/catalina.sh",'run']

