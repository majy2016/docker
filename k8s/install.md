windows powershell
1. 执行
$env:chocolateyUseWindowsCompression = 'true'

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

2. 执行

iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex



choco install minikube

minikube start

minikube dashboard


Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
