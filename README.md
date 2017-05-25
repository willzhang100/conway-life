I made a basic program that runs Conway's Game of Life using the tkinter module in Python.

Conway's Game of Life is a famous example of a cellular automaton. The game takes place in
a 2D grid of square cells. Each cell is considered either dead (white) or alive (black). 

There are four simple rules to the Game of Life:
1. If a cell is alive and has less than two live neighbors, then the cell will die (death by underpopulation).
2. If a cell is alive and has more than three live neighbors, then the cell will die (death by overpopulation).
3. If a cell is dead and has exactly three live neighbors, then the cell will become alive again (birth by reproduction).
4. If a cell is alive and has two or three live neighbors, then the cell will continue living.

Based off of these four rules, the pattern of the next generation of cells can be rendered.
I made some example "seeds," which are initial states for the game to load and run. You can
make your own seed files by creating a text file and typing out a square grid of 0's (dead cells) and 1's (alive cells). 
In the life.py file, change the value of the path variable to the path of the file you want to run.
