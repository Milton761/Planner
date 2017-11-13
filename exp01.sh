#!/bin/bash


declare -a arr=(
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem01.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem02.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem03.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem04.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem05.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem06.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem07.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem08.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem09.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem10.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem11.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem12.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem13.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem14.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem15.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem16.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem17.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem18.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem19.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem20.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem21.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem22.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem23.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem24.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem25.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem26.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem27.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem28.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem29.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/boxes/problem30.pddl'
	)

for i in "${arr[@]}"
do
	timeout $2 python3 planner.py -dfs 'pddl/robot/domain.pddl' $i >> $1
   	if [ $? -ne 0 ]
	then
		fullfilename=$i
		filename=$(basename "$fullfilename")
		fname="${filename%.*}"
		
		echo "$fname      -1          -1      -1         -1         -1      -1      -1" >> $1
	fi
done

