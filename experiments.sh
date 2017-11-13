#!/bin/bash

echo $1 
echo $2
echo $3


echo -e "\nH_ADD"
time  timeout $3  python3 planner.py -A* $1 $2 H -h_add
echo -e "\nH_MAX"
time timeout $3  python3 planner.py -A* $1 $2 H -h_max 
echo -e "\nH_FF"
time timeout $3  python3 planner.py -A* $1 $2 H -h_ff 
echo -e "\nDFS"
time timeout $3  python3 planner.py -dfs $1 $2 
echo -e "\nBFS"
time timeout $3  python3 planner.py -bfs $1 $2 
