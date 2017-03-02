#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

RUN \
	yum -y install wget && \
	#yum -y update && \
	wget http://dev.mysql.com/get/mysql57-community-release-el6-9.noarch.rpm && \
	yum -y install mysql57-community-release-el6-9.noarch.rpm && \
	sed -i "27s/enabled=0/enabled=1/g" /etc/yum.repos.d/mysql-community.repo && \
	sed -i "34s/enabled=1/enabled=0/g" /etc/yum.repos.d/mysql-community.repo && \
    yum -y install mysql-community-server


RUN /etc/init.d/mysqld start &&\
    mysql -e "grant all privileges on *.* to 'root'@'%' identified by 'majiayang';"&&\
    mysql -e "grant all privileges on *.* to 'root'@'localhost' identified by 'majiayang';"

#port
EXPOSE 3306

#start cmd
#CMD ["/usr/bin/mysqld_safe"]

