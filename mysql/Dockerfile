#Vsersion 0.1

#base image
FROM daocloud.io/centos:6

#au
MAINTAINER majy<majiayang@zuozh.com>

RUN \
#	yum -y update && \
	yum -y install mysql-server

RUN /etc/init.d/mysqld start &&\
    mysql -e "grant all privileges on *.* to 'root'@'%' identified by 'letmein';"&&\
    mysql -e "grant all privileges on *.* to 'root'@'localhost' identified by 'letmein';"&&\
    mysql -u root -pletmein -e "show databases;"

#port
EXPOSE 3306

#start cmd
#CMD ["/usr/bin/mysqld_safe"]

