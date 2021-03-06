FROM openjdk:8-jdk

RUN apt-get update && apt-get install -y git curl vim python-dev libssl-dev build-essential libssl-dev&& rm -rf /var/lib/apt/lists/*

ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

#ARG user=jenkins
#ARG group=jenkins
#ARG uid=1000
#ARG gid=1000

# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container, 
# ensure you use the same uid
#RUN groupadd -g ${gid} ${group} \
#    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

# Jenkins home directory is a volume, so configuration and build history 
# can be persisted and survive image upgrades
VOLUME /var/jenkins_home

# `/usr/share/jenkins/ref/` contains all reference configuration we want 
# to set on a fresh new installation. Use it to bundle additional plugins 
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

ENV TINI_VERSION 0.14.0
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd

# Use tini as subreaper in Docker container to adopt zombie processes 
RUN curl -fsSL https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static-amd64 -o /bin/tini && chmod +x /bin/tini \
  && echo "$TINI_SHA  /bin/tini" | sha256sum -c -

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

# jenkins version being bundled in this docker image
ARG JENKINS_VERSION
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.46.1}

# jenkins.war checksum, download will be validated using it
ARG JENKINS_SHA=33a3f4d983c6188a332291e1d974afa0a2ee96a0ae3cb6dd4f2098086525f9f1

# Can be used to customize where jenkins.war get downloaded from
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war

# could use ADD but this one does not check Last-Modified header neither does it allow to control checksum 
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \
  && echo "${JENKINS_SHA}  /usr/share/jenkins/jenkins.war" | sha256sum -c -

ENV JENKINS_UC https://updates.jenkins.io
RUN chown -R root "$JENKINS_HOME" /usr/share/jenkins/ref

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

USER root

COPY jenkins-support /usr/local/bin/jenkins-support
COPY jenkins.sh /usr/local/bin/jenkins.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh
COPY install-plugins.sh /usr/local/bin/install-plugins.sh

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /root/.jenkins
RUN mkdir /opt/maven
RUN git config --global user.name "majiayang"
RUN git config --global user.email majiayang@zuozh.com
COPY apache-maven-3.3.9-bin.tar.gz /root/pkg/
COPY pip-9.0.1.tar.gz /root/pkg/
RUN tar -zxvf ~/pkg/apache-maven-3.3.9-bin.tar.gz -C /opt/maven --strip-components 1
RUN tar -zxvf ~/pkg/pip-9.0.1.tar.gz -C /root/pkg/
RUN wget http://peak.telecommunity.com/dist/ez_setup.py
RUN python ez_setup.py
RUN python /root/pkg/pip-9.0.1/setup.py install
RUN pip install paramiko
RUN pip install configparser
ENV MAVEN_HOME /opt/maven
ENV PATH ${MAVEN_HOME}/bin:$PATH
RUN apt-get install -y npm
RUN apt-get install -y nodejs-legacy
RUN npm install -g n
RUN n latest
RUN export PATH=$PATH:/var/jenkins_home/phantomjs-2.1.1-linux-x86_64/bin/
RUN export PATH=$PATH:/usr/local/n/versions/node/8.1.4/bin/
