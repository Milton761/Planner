#!/bin/bash


declare -a arr=(
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem01.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem02.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem03.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem04.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem05.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem06.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem07.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem08.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem09.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem10.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem11.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem12.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem13.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem14.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem15.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem16.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem17.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem18.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem19.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem20.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem21.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem22.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem23.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem24.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem25.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem26.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem27.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem28.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem29.pddl'
	'/home/milton/Documentos/parser-pddl/python/EP03/pddl/robot/rooms/problem30.pddl'
	)



for i in "${arr[@]}"
do
	timeout $2 python3 planner.py -bfs 'pddl/robot/domain.pddl' $i  >> $1
   	if [ $? -ne 0 ]
	then
		fullfilename=$i
		filename=$(basename "$fullfilename")
		fname="${filename%.*}"
		
		echo "$fname      -1          -1      -1         -1         -1      -1      -1" >> $1
	fi
done

