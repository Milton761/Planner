#!/usr/bin/env gnuplot

set terminal pdf
set output 'rooms_time.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Time"
set grid y
set grid x
set logscale y 10

set ylabel "Time (seconds)"


plot "h_ff_room.dat" using 2:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 2:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 2	:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 2:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 2:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal pdf
set output 'rooms_cost.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Cost"
set grid y
set grid x



set ylabel "Cost"


plot "h_ff_room.dat" using 3:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 3:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 3:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 3:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 3:xtic(1) t "dfs" with linespoints pt 14 ps 0.8





set terminal pdf
set output 'rooms_htime.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Heuristic Time"
set grid y
set grid x



set ylabel "Time (seconds)"


plot "h_ff_room.dat" using 4:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 4:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 4:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 4:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 4:xtic(1) t "dfs" with linespoints pt 14 ps 0.8





set terminal pdf
set output 'rooms_stVisited.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs States Visited"
set grid y
set grid x



set ylabel "# States"


plot "h_ff_room.dat" using 5:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 5:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 5:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 5:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 5:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal pdf
set output 'rooms_stExpanded.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs States Expanded"
set grid y
set grid x


set ylabel "# States"


plot "h_ff_room.dat" using 6:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 6:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 6:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 6:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 6:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal pdf
set output 'rooms_bFactor.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Average Branch Factor"
set grid y
set grid x



set ylabel "branch factor"


plot "h_ff_room.dat" using 7:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 7:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 7:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 7:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 7:xtic(1) t "dfs" with linespoints pt 14 ps 0.8






set terminal pdf
set output 'rooms_penetrance.pdf'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Penetrance"
set grid y
set grid x



set ylabel "penetrance"


plot "h_ff_room.dat" using 8:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_room.dat" using 8:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_room.dat" using 8:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_room.dat" using 8:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_room.dat" using 8:xtic(1) t "dfs" with linespoints pt 14 ps 0.8
