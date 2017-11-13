from pddlparser import PDDLParser
from copy import deepcopy
import sys, getopt



# [4 4 2] -> 32 
def tam_instances(vector_param_len):

	final_tam = 1
	for tam in vector_param_len:
		final_tam = final_tam*tam
	
	return final_tam


OBJ = {'block' : ['d', 'b', 'a', 'c']}

TEST = {'b1' : ['a', 'b', 'c'] , 
		'b2' : ['x', 'y',] ,
		'b3' : ['1','2']}

#headers_tyoes is a vector of types : [block, blockB]
#objects is a dictionary that contains the posibles values of the types : {'block' : ['d', 'b', 'a', 'c']}

def gen_all_combinations(headers_types ,objects):

	#print("init function")

	vector_freq = []

	instances_values = []

	index = []

	num_values = []
	keys = {}

	i=0
	for tp in headers_types:


		num_values.append(len(objects[tp]))
		index.append(0)
		keys[i] = tp
		i = i+1


		#print(tp)
	#print(num_values)
	#print(len(num_values))
	for i in range(1,len(num_values)):

		n = num_values[i]
		for j in range(i+1, len(num_values)):
			n = n*num_values[j]

		vector_freq.append(n)

		#print('here',i)

	vector_freq.append(1)

	#print(vector_freq)
	#print(index)

	full_tam = tam_instances(num_values)
	#print(full_tam)

	for i in range(full_tam):

		posb = [None]*len(vector_freq)

		for j in range(len(vector_freq)):
			

			posb[j] = objects[keys[j]][index[j]]

			if (i+1)%vector_freq[j] == 0:
				index[j] = (index[j]+1)%num_values[j]


		instances_values.append(posb)




	#print("end function")
	return instances_values



def instantiate_action(action, objects):

	number_params = len(action.params)

	var_names = [] 
	#var_names contains the name of the arg variables : ['?x', '?y', ...]
	for var in action.params:
		var_names.append(var.name)
	#print(var_names)

	headers = []

	for par in action.params:
		headers.append(par.type)

	#print(headers)

	all_values_instances = gen_all_combinations(headers, objects)
	

	R = []

	for i in range(len(all_values_instances)):

		temp_action = deepcopy(action)

		for index in range(len(action.params)):
			temp_action.params[index]._value = all_values_instances[i][index]
		
		R.append(temp_action)	
		#print('')


	for action in R:


		#change with a dict
		h = []
		v = []
		for i in range(len(action.params)):
			h.append(action.params[i].name)
			v.append(action.params[i].value)
		

		#print('-------------PRECONDITION---------------------')
	
		

		for i in range(len(action.precond)):

			literal =  action.precond[i]
			subs = {}
			for j in range(literal._predicate.arity):
				subs[literal._predicate.args[j]] = v[h.index(literal._predicate.args[j])]

			literal._predicate = literal._predicate.ground(subs)

		#	print(literal._predicate, literal.is_positive())

		#print('-------------EFFECT---------------------')

		for i in range(len(action.effects)):
			literal =  action.effects[i]
			subs = {}
			for j in range(literal._predicate.arity):
				subs[literal._predicate.args[j]] = v[h.index(literal._predicate.args[j])]

			literal._predicate = literal._predicate.ground(subs)

		#	print(literal._predicate, literal.is_positive())


	return R


	#for eff in action.effects:
	#	print(eff)


#A frontier is the structure used in the search, search_type(0 = stack),search_type(1 = queue) 


#insert a new element in the frontier, return the frontier updated
def insert(list, search_type, element):

	if(search_type == 0):
		list.append(element)
	if(search_type == 1):
		list.append(element)

	return list

#return  next element of the frontier
def top(list, search_type):

	if(search_type == 0):
		return list[-1]
	if(search_type == 1):
		return list[0]

#remove next element of the frontier, return the frontier updated
def pop(list, search_type):

	if(search_type == 0):
		list.pop(-1)
	if(search_type == 1):
		list.pop(0)
	return list

#return if the frontier is empty
def is_empty(list):
	if len(list)==0:
		return True
	else:
		return False


def ver_precond(precs, state):
	

	IS_VALID = True

	for p in precs:
		


		if p._predicate.name == '=':

			X = p._predicate.args[0]
			Y = p._predicate.args[1]


			if (str(X)==str(Y)) == p.is_positive():
				IS_VALID = True
			else:
				IS_VALID = False
				break

		else:

			if (str(p) in state):
				IS_VALID = True
			else:
				IS_VALID = False
				break;


	return IS_VALID



def generate_new_state(eff,state):

	#print(state)

	for ef in eff:


		if ef.is_positive():
			state = state.union({str(ef)})
		else:
			state = state.difference({str(ef._predicate)})

	#print(state)

	return state


def expand_state(state, action, objects):

	STATES = []

	ACT = []
	#state is a new posible state (an action instantiate)
	#verify if the new state is valid with the preconditions
	#if is valid update the effects and add in STATES


	#print(state)
	#print(objects)

	pos_states = instantiate_action(action, objects)

	for st in pos_states:

		precs =  st.precond

		if ver_precond(precs, state) == True:

			new_s  = generate_new_state(st.effects, state)

			STATES.append(new_s)

			ACT.append(st)

	return [STATES,ACT]




def print_policy(plan):

	for action in plan:
		print(action.name,'( ',end='')
		for p in action.params:
			print(p.value,end=' ')
		print(')')

	return 



def search(search_type, domain, problem):
	#P is a plan, a set of actions

	file = open('search_tree.dot','w')
	file.write('digraph graphname {\n') 

	SOLUTION = False
	P = []

	VISITED = []

	frontier = list()
	current_state = []

	#add init state to the frontier
	insert(frontier, search_type, [problem.init,[]])
	VISITED.append(problem.init)

	while is_empty(frontier) == False:

		current_state = top(frontier,search_type)

		
		str_state = str(VISITED.index(current_state[0])) 

		file.write(str_state)
		file.write(' [label="')
		file.write(str(current_state[0]))
		file.write('"];\n')

		file.write(str_state)
		file.write(' [shape = box];\n')
		if problem.goal.issubset(current_state[0]):
			SOLUTION = True
			P = current_state[1]
			break


		pop(frontier,search_type)


		#generate all new posibles states for each action

		for action in domain.operators:

			[STATES,ACT] = expand_state(current_state[0], action, problem.objects)


			for i in range(len(STATES)):

				if STATES[i] not in VISITED:

					tmp_sol = deepcopy(current_state[1])
					tmp_sol.append(ACT[i])
					
					file.write(str(VISITED.index(current_state[0])))

					insert(frontier,search_type,[STATES[i],tmp_sol])
					file.write(' -> ')

					VISITED.append(STATES[i])
					file.write(str(VISITED.index(STATES[i])))



					file.write(' [label = "')
					file.write(ACT[i].name)
					file.write(' ')

					
					for p in ACT[i].params:
						file.write(p.value)
						file.write(' ')
					file.write('"]')


					file.write(';\n')
					


	file.write('}')
	print("Solution: ",SOLUTION)
	return P


#plan = search(0,domain,problem)

#print_policy(plan)

def main(argv):
	#print(argv)

	search_type = argv[0]
	domain_path = argv[1]
	problem_path = argv[2]

	TYPES = ['-dfs','-bfs']



	if search_type not in TYPES:
		print('Not valid search' ,search_type)
		print('VALID SEARCH : -dfs, -bfs')
		return
	else:
		search_type = TYPES.index(search_type)
		#print(search_type)

		#domain = PDDLParser.parse("pddl/blocksworld/domain.pddl")
		#problem = PDDLParser.parse("pddl/blocksworld/problems/probBLOCKS-04-0.pddl")

		domain = PDDLParser.parse(domain_path)
		problem = PDDLParser.parse(problem_path)


		plan = search(search_type, domain, problem)
		print_policy(plan)

	return

if __name__ == "__main__":
   main(sys.argv[1:])