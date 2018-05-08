# gitagent

Instructions on how to run multi-agent simulations.

Modify the following paths in the following files to your preferred destination:

mylogging.py ---> line 5, 7, and 9.

simulation.py ---> line 246, 339, and 391.

msg_PUnit.py ---> line 98, and 103.

agent_run.py ---> 302, 307, and 361.

Create the following folders:

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/enemy/same/30ag/

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/enemy/same/10ag/

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/friend/same/30ag/

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/friend/same/10ag/

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/half/same/30ag/

~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/half/same/10ag/

Copy the /result_scripts/init_4.sh file into the catkin_ws folder and run it.

./init_4.sh

In order to visualize the results run:

./plot_script.sh






