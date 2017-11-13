from pddlparser import PDDLParser
from copy import deepcopy
import sys, getopt
from util import *
import queue
import math
import time


class Planner:	


	def __init__(self, domain):

		self.domain = domain
		self.plan = []

		def empty_h(s,g):
			return 0

		self.heuristic = empty_h 

	def setHeuristic(self, heuristic):

		self.heuristic = heuristic

	def setProblem(self, problem):
		self.problem = problem

	def setFrontier(self, frontier):
		self.frontier = frontier

	def Heuristic(self, *args):
		return self.heuristic(*args)
	
	def emptyH(self,s,g):
		return 0

	def print_policy(self, plan):

		for action in plan:
			print(action.name,'( ',end='')
			for p in action.params:
				print(p.value,end=' ')
			print(')')

		return 


	def search(self):

		SOLUTION = False
		P = []
		VISITED = []

		frontier = self.frontier
		current_state = []

		#add init state to the frontier
		#[heuristic_value, current_state, current_plan]
		#[0, problem.init, []]
		frontier.put([ 0, problem.init, []])
		VISITED.append(problem.init)

		while frontier.empty() == False:

			current_state = frontier.get()


			str_state = str(VISITED.index(current_state[1])) 


			if problem.goal.issubset(current_state[1]):
				SOLUTION = True
				P = current_state[2]
				self.plan = P
				break


			#generate all new posibles states for each action

			for action in domain.operators:

				[STATES,ACT] = expand_state(current_state[1], action, problem.objects)


				for i in range(len(STATES)):

					if STATES[i] not in VISITED:

						tmp_sol = deepcopy(current_state[2])
						tmp_sol.append(ACT[i])
						
						
						#print("--------START H_ADD---------")
						hrst = self.Heuristic(current_state[1], problem.goal)
						#print(hrst)

						frontier.put([hrst, STATES[i],tmp_sol])

					

						VISITED.append(STATES[i])

		self.plan = P
		return P



	def h_add(self, current_state, goal_state):


		#optimize for relax the problem just once time
		relaxP = relaxProblem(self.domain)

		#s = goal_state
		H = {} 


		##init values for the DP

		for p in goal_state:

			if p in current_state:
				H[p] = 0
			else:
				H[p] = math.inf

		##end init values

		U = deepcopy(current_state)
		#print('U', U)
		
		while True:

			U_before = deepcopy(U)

			#print('U_before', U_before)
			#print('H',H)
			#input()

			for action in relaxP.operators:

				#print('for action', str(action))


				all_pos_action = instantiate_action(action, self.problem.objects)

				for act in all_pos_action:



					if ver_precond(act.precond, U):

						#print("ACTION PASS : ", str(act))

						U = generate_new_state(act.effects, U)

						for p in act.effects:

							#print(p)

							to_sum = []

							for q in act.precond:
								
								if q in H:
									to_sum.append(H[str(q)])
								else:
									to_sum.append(0)


							if p not in H:
								H[str(p)] = math.inf

							H[str(p)] = min( H[str(p)], 1 +  sum( to_sum ) )

		
			if U_before == U:
				#print('fixed point')
				break



		return sum( [H[p] for p in current_state] )

		



		

	def h_max(self, current_state, goal_state):
		#optimize for relax the problem just once time
		relaxP = relaxProblem(self.domain)

		#s = goal_state
		H = {} 


		##init values for the DP

		for p in goal_state:

			if p in current_state:
				H[p] = 0
			else:
				H[p] = math.inf

		##end init values

		U = deepcopy(current_state)
		#print('U', U)
		
		while True:

			U_before = deepcopy(U)

			#print('U_before', U_before)
			#print('H',H)
			#input()

			for action in relaxP.operators:

				#print('for action', str(action))


				all_pos_action = instantiate_action(action, self.problem.objects)

				for act in all_pos_action:



					if ver_precond(act.precond, U):

						#print("ACTION PASS : ", str(act))

						U = generate_new_state(act.effects, U)

						for p in act.effects:

							#print(p)

							to_sum = []

							for q in act.precond:
								
								if q in H:
									to_sum.append(H[str(q)])
								else:
									to_sum.append(0)


							if p not in H:
								H[str(p)] = math.inf

							H[str(p)] = min( H[str(p)], 1 +  sum( to_sum ) )

		
			if U_before == U:
				#print('fixed point')
				break



		return max( [H[p] for p in current_state] )





#SINGLE TEST
#SET PATH TO OTHERS PROBLEMS!

domain = PDDLParser.parse('pddl/robot/domain.pddl')
problem = PDDLParser.parse('pddl/robot/boxes/problem05.pddl')

#TO RUN A PROBLEM
#1. CREATE A PLANNER WITH A DOMAIN
#2. SET PROBLEM TO THE PLANNER
#3. SET HEURISTIC TO THE PLANNER,(DEFAULT HEURISTIC THAT RETURN 0)
#4. SET FRONTIER(STACK, QUEUE OR PRIORITY QUEUE)
#5. RUN PLANNER

#EXAMPLE 

P = Planner(domain)
P.setProblem(problem)


#PLANNER WITH HEURISTIC H_ADD, USING A PRIORITY QUEUE#
print('PQ - H_ADD')
P.setHeuristic(P.h_add)
P.setFrontier(queue.PriorityQueue())

t = time.process_time()
plan = P.search()
elapsed_time = time.process_time() - t
print(elapsed_time)

#PLANNER WITH HEURISTIC H_MAX, USING A PRIORITY QUEUE#
print('PQ - H_MAX')
P.setHeuristic(P.h_max)
P.setFrontier(queue.PriorityQueue())

t = time.process_time()
plan = P.search()
elapsed_time = time.process_time() - t
print(elapsed_time)



#PLANNER WITHOUT HEURISTIC , USING A QUEUE#
print('QUEUE')

P.setHeuristic(P.emptyH)
P.setFrontier(queue.Queue())
t = time.process_time()
plan = P.search()
elapsed_time = time.process_time() - t
print(elapsed_time)


#PLANNER WITHOUT HEURISTIC , USING A STACK#
print('STACK')

P.setHeuristic(P.emptyH)
P.setFrontier(queue.LifoQueue())
t = time.process_time()
plan = P.search()
elapsed_time = time.process_time() - t
print(elapsed_time)




