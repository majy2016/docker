#!/usr/bin/python
#--coding:utf8--  
import sys,paramiko,configparser

class Pu(object):

    def __init__(self):
        self.port = 22
        self.user = "root"
        self.password = "zzjr#2015"
        self.file = "host.conf"
        self.params = sys.argv
        self.project = self.params[1]
        self.env_type = self.params[2]
        self.local = "/var/jenkins_home/workspace/%s/default/%s-webapp/target/%s.war"%(self.project,self.project,self.project)
        # self.local = "/Users/majy/Documents/code/docker/jenkins/jenkins.sh"
        self.remote = "/usr/local/tomcat/webapps/ROOT.war"

    def get_project(self):
        params = sys.argv
        return self.params[1]

    def get_host(self):
        if self.env_type == "jiesuan":
            print "project is :%s , env is %s" % (self.project, self.env_type)
            settings = configparser.ConfigParser()
            settings.read(self.file)
            return settings.get(self.env_type,self.project)
        else:
            print "env : %s is not support ------------------"%self.env_type

    def ssh_connect(self):
        print "ssh connect host is : %s"%(host)
        try:
            sc = paramiko.SSHClient()
            sc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sc.connect(hostname=host,port=self.port,username=self.user,password=self.password)
            self.__connect = sc
        except Exception as e:
            print "connect ssh env error ---------!",e

    def sftp_connect(self):
        print "sftp connect host is : %s" % (host)
        try:
            transport = paramiko.Transport(host,self.port)
            transport.connect(username=self.user,password=self.password)
            self.__transport = transport
        except Exception as e:
            print "connect sftp env error ---------!",e

    def ssh_command(self,commands):
        for command in commands:
            stdin,stdout,stderr = self.__connect.exec_command(command)
            print "shell command result :",stdout.readlines()

    def ssh_upload(self):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(localpath=self.local,remotepath=self.remote)
        self.__transport.close()

    def ssh_close(self):
        self.__connect.close()


if __name__ == '__main__':
    pu = Pu()
    host = pu.get_host()
    pu.ssh_connect()
    commands_1 = ["""
    ID=$(ps -ef | grep -v grep |  grep  tomcat |grep java |awk '{print $2}')
echo $ID
if [ "$ID" = "" ]
then
    echo "no tomcat -----"
else
for id in $ID
do
echo "kill id:$id----"
kill -9 $id
done
fi""",
                  "rm -rf /usr/local/tomcat/webapps/*"]
    pu.ssh_command(commands_1)
    print "upload -------------"
    pu.sftp_connect()
    pu.ssh_upload()
    print pu.get_project()
    if pu.get_project() == "tengu" or pu.get_project() == "dragon":
        commands_2 = ["service tomcat start"]
    else:
        commands_2 =["cd /usr/local/tomcat/bin/&&./startup.sh"]
    print "start ---------------"
    pu.ssh_command(commands_2)
    pu.ssh_close()





