import argparse
from pddlparser import PDDLParser
from util import *

domain = PDDLParser.parse('pddl/tetris-opt14-strips/domain.pddl')
problem = PDDLParser.parse('pddl/tetris-opt14-strips/p01-10.pddl')



def foo():

	def sub_foo():
		print("sub_foo")


	sub_foo()


foo()



d = relaxProblem(domain)


for action in d.operators:

	for eff in action.effects:
		print(eff)
	print("------------------------")

