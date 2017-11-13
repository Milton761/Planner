from pddlparser import PDDLParser
from copy import deepcopy
import sys, getopt



# [4 4 2] -> 32 
def tam_instances(vector_param_len):

	final_tam = 1
	for tam in vector_param_len:
		final_tam = final_tam*tam
	
	return final_tam

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


##--------utils for EP2 --------------------------

#domain that ignore negative effects
def relaxProblem(domain):

	relaxP = deepcopy(domain)

	for action in relaxP.operators:

		relaxEff = [effect for effect in action.effects if effect.is_positive()]
		action._effects = relaxEff

	return relaxP


def firstLevel(var, listVar):

	level = 0
	for Var in listVar:
		if var in Var:
			return level
		level = level + 1
	return -1
