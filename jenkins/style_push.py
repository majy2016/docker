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
        self.local = "/var/jenkins_home/workspace/%s/%s.tar.gz"%(self.project,self.project)
        # self.local = "/Users/majy/Documents/code/docker/jenkins/jenkins.sh"

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

    def ssh_upload(self,remote):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(localpath=self.local,remotepath=remote)
        self.__transport.close()

    def ssh_close(self):
        self.__connect.close()


if __name__ == '__main__':
    pu = Pu()
    host = pu.get_host()
    pj = pu.get_project()
    if pj =="style":
        commands_1 = ["rm -rf /home/zzjr/style/trunk/*"]
        commands_2 = ["cd /home/zzjr/style/trunk&&tar -zxvf x.tar.gz"]
        remote = "/home/zzjr/style/trunk/x.tar.gz"
    elif pj =="admin":
        commands_1 = ["rm -rf /usr/local/admin/*"]
        commands_2 = ["cd /usr/local/admin&&tar -zxvf x.tar.gz --strip-components 1"]
        remote = "/usr/local/admin/x.tar.gz"
    elif pj =="m2"
    pu.ssh_connect()
    pu.ssh_command(commands_1)
    print "upload -------------"
    pu.sftp_connect()
    pu.ssh_upload(remote)
    print "tar -------------"
    pu.ssh_command(commands_2)
    pu.ssh_close()