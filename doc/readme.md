commit 镜像：
commit 主要用于通过差异性，创建一个新的image
Usage: docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]Create a new image from a container's changes

  -a, --author=""     Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
  -m, --message=""    Commit message
  -p, --pause=true    Pause container during commit



  docker commit -a "majy" -m='zzjr jenkins' fa2c70698bbe zzjr/jenkins:1.0.0

  docker tag zzjr/jenkins:1.0.0 majiayang/zzjr-jenkins:1.0.0

  docker login

  docker push zzjr/jenkins:1.0.0