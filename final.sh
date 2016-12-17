############################# CLOUDERA #########################################
######## This script executes the migration strategy and accordingly  ##########
######## migrates the containers from one VM to another VM using the  ##########
########     migrate script which runs if value returned is 1         ##########
#########################   ./final.sh      #################################### 
################################################################################
#! /bin/bash
# execute the migrationstrategy snippet and store the value
var=$(python MigrationStrategy.py)
# if value returned is 1, migrate, else do not migrate
if [ $var==1 ]  
then 
	./migrate.sh
else 
	echo "No need to migrate"
fi
