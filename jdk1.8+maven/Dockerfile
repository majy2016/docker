FROM openjdk:8-jdk

ENV TZ=Asia/Shanghai

ENV JAVA_HOME /usr/local/openjdk-8
ENV PATH ${JAVA_HOME}/bin:$PATH

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /opt/maven
COPY apache-maven-3.6.1-bin.tar.gz /root/pkg/
RUN tar -zxvf ~/pkg/apache-maven-3.6.1-bin.tar.gz -C /opt/maven --strip-components 1
ENV MAVEN_HOME /opt/maven
ENV PATH ${MAVEN_HOME}/bin:$PATH