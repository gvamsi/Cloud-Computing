############################# CLOUDERA #########################################
######## This script executes the zipped contianer and displays the   ##########
########       iamge name to the user which needs to be run           ##########
#########################     ./run.sh      ################################### 
################################################################################

#! /bin/bash
# load the zipped container onto docker
var="$(ls -1 --sort none *.tar | head -n 1)"
docker load -i $var


