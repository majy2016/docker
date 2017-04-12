#!/bin/bash
pwd

echo $projects

projects=${projects//,/ }

for project in $projects   
do  
	echo  ------------  now publish $project ----------------------\n
    python /var/jenkins_home/push.py $project $evn
done  