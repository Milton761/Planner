
Authors: 
-Milton Condori
-Henrique Donancio

Parser by:
-Thiago Pereira

usage: python3 planner.py <search_type> <domain_path> <problem_path> H <heuristic>


positional arguments:
  search_type :type of search [-dfs,-bfs,-A*]
  domain      :path to PDDL domain file
  problem     :path to PDDL problem file

Option:
  H:
  heuristic : type of heuristic [-h_add,-h_max,-f_add]
# Examples:
bash
$ python3 planner.py -A* pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl  H -h_add

$ python3 planner.py -A* pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl  H -h_max

$ python3 planner.py -A* pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl  H -h_ff

$ python3 planner.py -dfs pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl  

$ python3 planner.py -bfs pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl  


################################################################################################################################

to run a experiment (all searchs with a problem):
execute the script "experiments.sh"

usage : <domain_path> <problem_path> <time>

Example:

bash
$ ./experiments.sh pddl/robot/domain.pddl pddl/robot/boxes/problem05.pddl 10s


