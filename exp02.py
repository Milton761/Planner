from planner import Planner
import queue
from pddlparser import PDDLParser

domain = PDDLParser.parse('pddl/robot/domain.pddl')

#problems rooms

problem_path = [
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem01.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem02.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem03.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem04.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem05.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem06.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem07.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem08.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem09.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem10.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem11.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem12.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem13.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem14.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem15.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem16.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem17.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem18.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem19.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem20.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem21.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem22.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem23.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem24.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem25.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem26.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem27.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem28.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem29.pddl',
'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem30.pddl'
]


P = Planner(domain)

it = 1
for p in problem_path:
	problem = PDDLParser.parse(p)
	P.setProblem(problem)
	P.setFrontier(queue.PriorityQueue())
	P.setHeuristic(P.h_ff)
	[Plan, Time, Cost, HeuristicTime, StVisited, Expanded, BrachFactor, Penetrancy] = P.search()
	print(
	'% 10.3f' % it,	
	'% 10.3f' % Time,
	'% 10.0f' %  Cost,
	'% 10.3f' %  HeuristicTime,
	'% 10.0f' %  StVisited,
	'% 10.0f' %  Expanded,
	'% 10.3f' %  BrachFactor,
	'% 10.3f' %  Penetrancy
	)
	it = it+1
