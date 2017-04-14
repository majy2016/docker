#!/bin/bash
pwd

echo $projects

projects=${projects//,/ }

for project in $projects   
do  
	echo  ------------  now publish $project ----------------------\n
    python /var/jenkins_home/push.py $project $evn
done



# groovy

node{
env.build_name = build_name
env.release_branch = release_branch
def build_names = build_name.split(",")
for(i=0;i<build_names.size();i++){
        def job = build_names[i]
        def job_name = job+'-deploy'
        def git_url = 'git@gitlab.lark.wiki:nbgold/'+job+'.git'
        println "start build:"+job +'  '+release_branch
        build job: job, parameters: [string(name: 'git_url', value: git_url), string(name: 'git_name', value: job), string(name: 'release_branch', value: release_branch)]
        //build job: 'cms', parameters: [string(name: 'git_url', value: 'git@gitlab.lark.wiki:nbgold/cms.git'), string(name: 'git_name', value: 'cms'), string(name: 'release_branch', value: 'master')]
}
}


#sonar
sonar.projectKey=$git_name
sonar.projectName=$git_name
sonar.projectVersion=$release_branch
sonar.sourceEncoding=UTF-8
sonar.language=java
sonar.sources=.