#!/usr/bin/env gnuplot

set terminal svg enhanced background rgb 'white'
set output 'boxes_time.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Time"
set grid y
set grid x
set logscale y 10

set ylabel "Time (seconds)"


plot "h_ff_box.dat" using 2:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 2:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 2	:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 2:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 2:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal svg enhanced background rgb 'white'
set output 'boxes_cost.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Cost"
set grid y
set grid x



set ylabel "Cost"


plot "h_ff_box.dat" using 3:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 3:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 3:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 3:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 3:xtic(1) t "dfs" with linespoints pt 14 ps 0.8





set terminal svg enhanced background rgb 'white'
set output 'boxes_htime.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Heuristic Time"
set grid y
set grid x



set ylabel "Time (seconds)"


plot "h_ff_box.dat" using 4:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 4:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 4:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 4:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 4:xtic(1) t "dfs" with linespoints pt 14 ps 0.8





set terminal svg enhanced background rgb 'white'
set output 'boxes_stVisited.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs States Visited"
set grid y
set grid x



set ylabel "# States"


plot "h_ff_box.dat" using 5:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 5:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 5:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 5:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 5:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal svg enhanced background rgb 'white'
set output 'boxes_stExpanded.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs States Expanded"
set grid y
set grid x


set ylabel "# States"


plot "h_ff_box.dat" using 6:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 6:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 6:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 6:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 6:xtic(1) t "dfs" with linespoints pt 14 ps 0.8




set terminal svg enhanced background rgb 'white'
set output 'boxes_bFactor.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Average Branch Factor"
set grid y
set grid x



set ylabel "branch factor"


plot "h_ff_box.dat" using 7:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 7:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 7:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 7:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 7:xtic(1) t "dfs" with linespoints pt 14 ps 0.8






set terminal svg enhanced background rgb 'white'
set output 'boxes_penetrance.svg'

set xtics rotate # crucial line

set key vert
set key left 

  

set title "Problem vs Penetrance"
set grid y
set grid x



set ylabel "penetrance"


plot "h_ff_box.dat" using 8:xtic(1) t "h_{ff}" with linespoints pt 4 ps 0.6, "h_add_box.dat" using 8:xtic(1) t "h_{add}" with linespoints pt 6 ps 0.8, "h_max_box.dat" using 8:xtic(1) t "h_{max}" with linespoints pt 8 ps 0.8, "bfs_box.dat" using 8:xtic(1) t "bfs" with linespoints pt 12 ps 0.8, "dfs_box.dat" using 8:xtic(1) t "dfs" with linespoints pt 14 ps 0.8
