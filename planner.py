from pddlparser import PDDLParser
from copy import deepcopy
import sys, getopt
from util import *
import queue
import math
import time
import os



class Planner:	


	def __init__(self, domain):

		self.domain = domain
		self.plan = []

		def empty_h(s,g):
			return 0

		self.heuristic = empty_h 
		self.relaxP = relaxProblem(domain)

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
		t = 1
		for action in plan:
			print(t,' ',action.name,' ( ',end='')
			for p in action.params:
				print(p.value,end=' ')
			print(')')
			t = t+1

		return 


	def search(self):

		Plan = None
		Time = None
		Cost = None
		HeuristicTime = 0
		BrachFactor = None
		StVisited = None
		BrachFactor = None
		Penetrancy = None

		SOLUTION = False
		P = []
		VISITED = []
		EXPANDED = 0	

		frontier = self.frontier
		current_state = []

		#add init state to the frontier
		#[heuristic_value, current_state, current_plan]
		#[0, problem.init, []]
		frontier.put([ 0, self.problem.init, []])
		VISITED.append(self.problem.init)

		t0_search = time.process_time()

		while frontier.empty() == False:

			current_state = frontier.get()


			str_state = str(VISITED.index(current_state[1])) 


			if self.problem.goal.issubset(current_state[1]):
				SOLUTION = True
				P = current_state[2]
				self.plan = P
				break


			#generate all new posibles states for each action

			for action in self.domain.operators:

				[STATES,ACT] = expand_state(current_state[1], action, self.problem.objects)
				EXPANDED = EXPANDED + len(STATES)
				

				for i in range(len(STATES)):

					if STATES[i] not in VISITED:

						tmp_sol = deepcopy(current_state[2])
						tmp_sol.append(ACT[i])
						
						
						
						t0_heuristic = time.process_time()
						hrst = self.Heuristic(current_state[1], self.problem.goal)
						t1_heuristic = time.process_time()
						
						HeuristicTime = HeuristicTime + (t1_heuristic - t0_heuristic)

						frontier.put([hrst, STATES[i],tmp_sol])

					

						VISITED.append(STATES[i])

		t1_search = time.process_time()



		self.plan = P

		Plan = P
		Time = t1_search - t0_search
		Cost = len(Plan)
		StVisited = len(VISITED)
		BrachFactor = EXPANDED/StVisited


		if EXPANDED == 0:
			Penetrancy = 1
		else:
			Penetrancy = Cost/EXPANDED


		return [Plan, Time, Cost, HeuristicTime, StVisited, EXPANDED, BrachFactor, Penetrancy]



	def h_add(self, current_state, goal_state):


		#optimize for relax the problem just once time
		relaxP = self.relaxP

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
		relaxP = self.relaxP

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

								#print("H",str(q))	
								#input()

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



	def h_ff(self, current_state, goal_state):


		relaxP = self.relaxP
		A = [None]
		F = []
		F.append(current_state)
		t = 0

	
		

		while goal_state.issubset(F[t]) == False:

			t = t+1

			A_t = []
			for action in relaxP.operators:

				all_pos_action = instantiate_action(action, self.problem.objects)

				

				for act in all_pos_action:
					if ver_precond(act.precond, F[t-1]):
						A_t.append(act)
		
			A.append(A_t)
			F.append(deepcopy(F[t-1]))	
			for act in A[t]:

				F[t] = generate_new_state(act.effects, F[t])

			if F[t] ==	 F[t-1]:
				print("Failure!!")
				return

		#print([F,A])

		#Extracting a Relaxed Plan

		result = 0

		if goal_state.issubset(F[-1]) == False:
			print("Failure in Extracting a Relaxed Plan H_FF")
			return 

		list_levels = []
		for g in goal_state:
			list_levels.append(firstLevel(g,F))



		M = max(list_levels)

		G = {}
		for t in range(M+1):

			G[t] = []


			for g in goal_state:
				if firstLevel(g,F) == t:
					G[t].append(g)

		
		for t in range(M,0,-1):

			#print("++++++++++++++++++++++++++++++++++++++ ", t)
			#input()

			for g_t in G[t]:

				a = None
				flag = False

				for i in range(1,len(A)):
					A_t = A[i]

					#print("ACtions ", A_t)

					for act in A_t:

						effects = []

						for eff in act.effects:
							effects.append(str(eff))

						#print("Gt ",g_t)
						#print("Effects", effects)
						#input()

						if g_t in effects:
							a = act
							result = result + 1
							flag = True
							break
					if flag:
						break


				for p in a.precond:
					
					

					if p._predicate.name!="=":
						#print("Index ", G[firstLevel(str(p),F)])
						G[firstLevel(str(p),F)] = list(set().union(G[firstLevel(str(p),F)],[str(p)]))


		#print("END", result)
		#input()
		return result





#SINGLE TEST
#SET PATH TO OTHERS PROBLEMS!


#domain = PDDLParser.parse('pddl/robot/domain.pddl')
#problem = PDDLParser.parse('pddl/robot/boxes/problem05.pddl')

#domain = PDDLParser.parse('pddl/blocksworld/domain.pddl')
#problem = PDDLParser.parse('pddl/blocksworld/problems/probBLOCKS-04-0.pddl')

#TO RUN A PROBLEM
#1. CREATE A PLANNER WITH A DOMAIN
#2. SET PROBLEM TO THE PLANNER
#3. SET HEURISTIC FOR THE PLANNER,(DEFAULT HEURISTIC RETURN 0)
#4. SET FRONTIER(STACK, QUEUE OR PRIORITY QUEUE)
#5. RUN THE PLANNER

#EXAMPLE 

#domain = PDDLParser.parse('pddl/robot/domain.pddl')
#problem = PDDLParser.parse('pddl/robot/boxes/problem06.pddl')


#1#P = Planner(domain)
#2#P.setProblem(problem)
#3#P.setHeuristic(P.h_ff)
#4#P.setFrontier(queue.PriorityQueue())
#5#plan = P.search()


#P.print_policy(plan)



def main(argv):
	#print(argv)

	search_type = argv[0]

	domain_path = argv[1]
	problem_path = argv[2]

	#print(len(argv))
	heuristic_type = 'None'
	if len(argv) > 3:
		heuristic_command = argv[3]
		heuristic_type = argv[4]

	TYPES_SEARCH = ['-dfs','-bfs','-A*']
	TYPER_HEURISTIC = ['-h_add', '-h_max', '-h_ff']



	if search_type not in TYPES_SEARCH:
		print('Not valid search' ,search_type)
		print('VALID SEARCH : -dfs, -bfs, -A*')
		return

	if len(argv) > 3:
		if heuristic_type not in TYPER_HEURISTIC:
			print('Not valid search' ,search_type)
			print('VALID HEURISTIC : -h_add, -h_max, -h_ff')
			return

		if heuristic_command!='H':
			print('Not valid command')
			print('Valid commad for heuristic: H')

	
	domain = PDDLParser.parse(domain_path)
	problem = PDDLParser.parse(problem_path)



	P = Planner(domain)
	P.setProblem(problem)
	

	if search_type == '-dfs':
		P.setFrontier(queue.LifoQueue())

	if search_type == '-bfs':
		P.setFrontier(queue.Queue())



	if search_type == '-A*':
		P.setFrontier(queue.PriorityQueue())

		if heuristic_type == '-h_add':
			P.setHeuristic(P.h_add)
		if heuristic_type == '-h_max':
			P.setHeuristic(P.h_max)
		if heuristic_type == '-h_ff':
			P.setHeuristic(P.h_ff)
	#print(search_type)

	#domain = PDDLParser.parse("pddl/blocksworld/domain.pddl")
	#problem = PDDLParser.parse("pddl/blocksworld/problems/probBLOCKS-04-0.pddl")

	
	

	[Plan, Time, Cost, HeuristicTime, StVisited, Expanded, BrachFactor, Penetrancy] = P.search()
	

	#print(search_type, heuristic_type, domain_path, problem_path, elapsed_time)
	#print("-----------------------------------------")
	#print("Time of Planner",Time)
	#print("-----------------------------------------")
	#print("Cost of solution",Cost)
	#print("-----------------------------------------")
	#print("Time of Heuristic",HeuristicTime)
	#print("-----------------------------------------")
	#print("Visited States",StVisited)
	#print("-----------------------------------------")
	#print("Expanded States",Expanded)
	#print("-----------------------------------------")
	#print("Branch Factor",BrachFactor)
	#print("-----------------------------------------")
	#print("Penetrancy",Penetrancy)
	#print("-----------------------------------------")
	#print("Plan")
	#print("-----------------------------------------")
	#P.print_policy(Plan)
	#print("-----------------------------------------")

	print(
		'#',
		'%20s' % 'Name',
		'%10s' % 'Time',
		'%10s' % 'Cost',
		'%10s' % 'Hrst-Time',
		'%10s' % 'st-Visited',
		'%10s' % 'st-Expnded',
		'%10s' % 'brch-Fact',
		'%10s' % 'Penetrancy',
	)

	base=os.path.basename(problem_path)

	print(
		' ',
		'% 20s' % os.path.splitext(base)[0],
		'% 10.3f' % Time,
		'% 10.0f' %  Cost,
		'% 10.3f' %  HeuristicTime,
		'% 10.0f' %  StVisited,
		'% 10.0f' %  Expanded,
		'% 10.3f' %  BrachFactor,
		'% 10.3f' %  Penetrancy
	)

	return

if __name__ == "__main__":
   main(sys.argv[1:])


