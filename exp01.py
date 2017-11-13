from planner import Planner
import queue
from pddlparser import PDDLParser
import signal
import time




domain = PDDLParser.parse('pddl/robot/domain.pddl')

#test DOMAIN ROBOT
#test PROBLEM BOXEX


problem_path = [
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem01.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem02.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem03.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem04.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem05.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem06.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem07.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem08.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem09.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem10.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem11.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem12.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem13.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem14.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem15.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem16.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem17.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem18.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem19.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem20.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem21.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem22.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem23.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem24.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem25.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem26.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem27.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem28.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem29.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem30.pddl'
]


P = Planner(domain)

it = 1
for p in problem_path:
	problem = PDDLParser.parse(p)
	P.setProblem(problem)
	P.setFrontier(queue.PriorityQueue())
	P.setHeuristic(P.h_ff)



	Solution = P.search()

	

	[Plan, Time, Cost, HeuristicTime, StVisited, Expanded, BrachFactor, Penetrancy] = Solution
	print(
	'% 2.0f' % it,	
	'% 10.3f' % Time,
	'% 10.0f' %  Cost,
	'% 10.3f' %  HeuristicTime,
	'% 10.0f' %  StVisited,
	'% 10.0f' %  Expanded,
	'% 10.3f' %  BrachFactor,
	'% 10.3f' %  Penetrancy
	)

	it = it+1

	action_process = Process(target=do_actions)
 
    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=5)
 
    # We terminate the process.
    action_process.terminate()
    print("Hey there! I timed out! You can do things after me!")


