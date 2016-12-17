#Cloudera

CSE546 FALL 2016 CLOUD COMPUTING PROJECT: Workload Prediciton for Cloud Computing Elasticity Mechanism

#Files
```sh
      FILE                        PURPOSE                               MODIFIED/NEW                COMMENTS        

MigrationStrategy.py:  The python script which containes the              NEW                     USING psutil we get the cpu data and predict
                       trigger stratery and workload prediciton                                   the workload and run the trigger strategy

cpu_util.py:           Uses the psutil library to fetch the            MODIFIED                   psutil library invoked
                       CPU time series data for a system        

patternMatching.py:    Preprocessing and match step for matching
                       the upcoming cpu data with the exisitng         MODIFIED                   pattern matching implemented 
                       data

trigger_strategy.py:   Based on workload we can migrate the            MODIFIED                   trigger_strategy implemented
                       containers or not       

dockersetup.sh:        Installation steps for docker                   MODIFIED                   docker setup script implememted, can install docker with this

migrate.sh:            Based on MigrationStrategy transfer the           NEW                      please edit the IP address of the desitnation machine to
                       continer to the other system                                               run on other systems.

final.sh:              Execute the MigrationStratergy and                                         
                       based on the value it returns excute              NEW                      the first script to execute the other tasks
                       migrate

run.sh:                Load the zipped container onto                    NEW                      the script to laod the zipped contianer on docker
                       docker in the destination machine

```

#EXECUTION STEPS
```sh
Step 1 Run dockersetup.sh on the source and destination machines. Post installation restart the system.
Step 2 In the source machine (devstack1) create cloudera directory and in destination machine (devstack2) create cloudera1 directory.
Step 3 Save final.sh, migration.py and MigrationStrategy.py in cloudera and run.sh in cloudera1 and give the execute permissions for the shell scripts.
Step 4 Run final.sh which will execute MigrationStrategy.py and based on the value it returns migrate.sh is executed and the control passes to destination VM.
Step 5 Run run.sh in cloudera1 in destination followed by *docker run -it prodready /bin/bash* whcih will execute the contianer image. 
Step 6 We can run the *docker images* in destination to see that the image ID is same as that of host VM.
```
#ALGORITHM 
```sh
Step 1: Getting CPU analyzing monitoring data of resources on cloud.cpu_util.py gets the real time cpu data of resoucres on cloud. This will go
as an input to step2.

Step 2: patternMatching.py: In this we take CPU monitoring data in the form of list. This file implemnts the pattern matching algorithm that 
performs the preprocessing and match step to get the predicted CPU time seris string. This goes as an input to step 3.

Step 3: trigger_strategy.py: In this step we implement the trigger strategy that achieves the cloud computing elasticity mechanism with minimum
scaling delay of resources on cloud.

Step 4: Docker step is triggered that initiates the migration of containers across machines
```