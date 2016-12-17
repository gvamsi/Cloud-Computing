############################# CLOUDERA #########################################
######## This script installs docker in the host machine upon running ##########
####################   ./dockersetup.sh    #####################################
################################################################################
#! /bin/bash
sudo apt-get update
#recive the docker key to install the docker project
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
# to install the latest docker engine
apt-cache policy docker-engine
sudo apt-get install -y docker-engine
# to give access to the user to run docker and add the user a member of the group
sudo systemctl status docker
sudo usermod -aG docker ubuntu
docker info