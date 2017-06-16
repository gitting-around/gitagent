#!/usr/bin/env bash
timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_30_1.0_0.0_0.05_0\|0_mem0_enemy.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/enemy/same/30ag/ \;

timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_30_1.0_0.0_0.05_0\|0_mem0_friend.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/friend/same/30ag/ \;

timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_30_1.0_0.0_0.05_0\|0_mem0_half.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/half/same/10ag/ \;

timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_10_1.0_0.0_0.05_0\|0_mem0_enemy.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/enemy/same/10ag/ \;

timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_10_1.0_0.0_0.05_0\|0_mem0_friend.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/friend/same/10ag/ \;

timeout 31m roslaunch ~/catkin_ws/src/gitagent/Launch/launch_agents_10_1.0_0.0_0.05_0\|0_mem0_half.launch
find . -name 'result*' -maxdepth 1 -type f -exec mv {} ~/catkin_ws/results/braitenberg_1/dynamic/nomem/pressure_0.05/half/same/10ag/ \;
