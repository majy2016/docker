#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

RUN \
	yum -y install wget && \
	wget http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm && \
	rpm -i mysql-community-release-el6-5.noarch.rpm && \
	sed -i '25 s/enabled=0/enabled=1/g' /etc/yum.repos.d/mysql-community-source.repo && \
	yum -y install mysql-community-server

RUN /etc/init.d/mysqld start &&\
    mysqladmin -u root password "majiayang"

#port
EXPOSE 3306

#start cmd
#CMD ["/usr/bin/mysqld_safe"]

