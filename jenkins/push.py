#!/usr/bin/python
#--coding:utf8--  
import sys,subprocess,os,datetime,paramiko,re  
local_path='/home/pangpeng/'  
nginx_web_path='/var/www/html/'  
tomcat_webapps_path='/usr/local/tomcat7/webapps/'  
backup_nginx_path='/tmp/backup_nginx/'  
backup_tomcat_app='/tmp/backup_tomcat_app/'  
username='root'  
port=22 #ssh port  
  
def web(web_dir,update_ip):  
    #creat remote backup_path  
    creat_backup_dir_cmd = 'mkdir '+backup_nginx_path  
    exec_cmd(update_ip,creat_backup_dir_cmd)  
  
    current_date = datetime.datetime.now().strftime("%Y%m%d%H%M")  
    cmd = 'mv '+nginx_web_path+web_dir+' '+backup_nginx_path+web_dir+'_'+current_date  
    #backup  
    exec_cmd(update_ip,cmd)  
    #upload file  
    upload_cmd = 'scp -r '+local_path+web_dir+' '+update_ip+':'+nginx_web_path  
    print(upload_cmd)  
    subprocess.Popen(upload_cmd,shell=True,stdout=subprocess.PIPE)  
    #change owner  
    #chmod_cmd='chown -R jujusport.jujusport '+nginx_web_path+web_dir  
    #exec_cmd(update_ip,chmod_cmd)  
  
def tomcat(tomcat_ip,app):  
  
    root_dir = re.split('\.',app)[0]  
    creat_backup_tomcat_app_cmd = 'mkdir '+backup_tomcat_app  
    current_date = datetime.datetime.now().strftime("%Y%m%d%H%M")  
    tomcat_cmd='pkill -15 java;sleep 5;'+'mv '+tomcat_webapps_path+app+' '+backup_tomcat_app+app+'_'+current_date  
    tomcat_cmd2='mv '+tomcat_webapps_path+root_dir+' '+backup_tomcat_app+root_dir+'_'+current_date  
    upload_cmd='scp '+local_path+app+' '+tomcat_ip+':'+tomcat_webapps_path  
    cmd='sudo -u jujusport /usr/local/tomcat7/bin/catalina.sh start'  
  
    #create backup dir  
    exec_cmd(tomcat_ip,creat_backup_tomcat_app_cmd)  
    #backup PacketName.war PacketName  
    exec_cmd(tomcat_ip,tomcat_cmd)  
    exec_cmd(tomcat_ip,tomcat_cmd2)  
    #upload file  
    subprocess.Popen(upload_cmd,shell=True,stdout=subprocess.PIPE)  
    print "upload done:"+upload_cmd  
    #start tomcat  
    exec_cmd(tomcat_ip,cmd)  
  
  
def exec_cmd(server_ip, cmd):  
    paramiko.util.log_to_file('/tmp/paramiko.log')  
    pkey='/root/.ssh/id_rsa'  
    key=paramiko.RSAKey.from_private_key_file(pkey)  
    s=paramiko.SSHClient()  
    s.load_system_host_keys()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    s.connect(server_ip,port,username,pkey=key)  
    try:  
        print server_ip+':'+cmd  
        stdin,stdout,stderr=s.exec_command(cmd)  
        print 'stdout:'+stdout.read()  
        print 'stderr:'+stderr.read()  
    except Exception, e:  
        print e  
    finally:  
        s.close()  
  
def cleanstore(server_ip,back_up_dir):  
    command = "find %s -type d -mtime +30 |xargs rm -fr" %(back_up_dir)  
    exec_cmd(server_ip,command)  
if __name__ == "__main__":  
    print  ''''' 
            example:deploy.py web v1 
            example:deploy.py tomcat 192.168.1.192 ROOT.war 
            '''  
    if (sys.argv[1] == 'web') and (sys.argv[2]=='v1'):  
        web("v1",'192.168.1.193')  
        cleanstore('192.168.1.193',backup_nginx_path)  
    elif (sys.argv[1] == 'tomcat') and (sys.argv[2]=='192.168.1.192'):  
        tomcat('192.168.1.192',sys.argv[3])  
        cleanstore('192.168.1.192',backup_tomcat_app)  
    elif (sys.argv[1] == 'tomcat') and(sys.argv[2]=='192.168.1.193'):  
        tomcat('192.168.1.193',sys.argv[3])  
        cleanstore('192.168.1.193',backup_tomcat_app)  
    else:  
        sys.exit(0)