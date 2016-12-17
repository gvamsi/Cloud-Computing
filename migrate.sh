############################# CLOUDERA #########################################
######## This script executes the migration strategy and accordingly  ##########
########       migrates the containers from one VM to another VM      ##########
#########################   ./migrate.sh     ################################### 
################################################################################
#! /bin/bash
# get the largest files to migrate from the zipped containers
filename="$(ls -1 --sort none *.tar | head -n 1)"
echo "Migration of container begins"
# secure copy the containers to the other machine where docker is installed
scp $filename 192.168.1.6:/home/ubuntu/cloudera1
echo "Migration completed"
# ssh to the machine so that the contianer can begin execution
ssh 192.168.1.6

