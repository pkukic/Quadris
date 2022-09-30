# Quadris

This repository contains the codes used to find an arbitrary number of _board solutions_ to the game Quadris. A _board solution_ is a configuration of the board in which each of the 21 polyomino shapes used in the game is used exactly once, and each of the $9 \cdot 9 = 81$ cells are covered by exactly one polyomino shape. Additionally, each board solution has to be **unique**, that is, unrecoverable from any previously found solution by any rotation or reflection of the board (there are 8 symmetry mappings of a square - 4 rotations and 4 reflections).

## Credits

First of all, credit where credit is due. This project wouldn't be possible without this paper:

> Marcus Garvie, John Burkardt, A new mathematical model for tiling     finite regions of the plane with polyominoes, Contributions to Discrete Mathematics, Volume 15, Number 2, July 2020.

And the corresponding open-source repository:

https://zenodo.org/record/6366101#.YzWwhdKxWus

All important parts of the code related to generating and displaying multiple solutions to the polyomino tiling problem (and thus to the Quadris puzzle game) are from this repository. I just adapted and extended these codes so that I can solve Quadris.

## Project structure
The project is divided into 3 parts:
1. `generator` - the MATLAB and Python scripts used for generating solutions to the Quadris puzzle
2. `solver` - here you can use `gui.py` to play with the solutions - given a partial solution of the board, this will find the whole solution of the board
3. `unique` - the generated solutions are stored here. Since this is too big to fit on Github, I encourage you to download this from Zenodo and unpack it:
    https://zenodo.org/record/7125509#.YzW3itKxWus

## State of the project

I consider this project mostly finished. On the machine `generator` was run on (Core i7-5600U, 16 GB RAM) `populate_solutions_dir` can find a new, **unique** solution of the board about every 1 - 3 seconds (I only ran it for 40k solutions, so 3 seconds per solve was the worst I got). Also, `gui.py` can find a solution to a partially solved board in less than 5 seconds (tested on a different machine - Ryzen 7 4700u, 24 GB RAM).

I haven't found **all** solutions to the puzzle because I don't want to wait too long and only have one machine with MATLAB installed, but I consider this to be a really nice proof-of-concept project.

## Requirements

First of all, make sure you have MATLAB R2022b or higher installed. 
Instructions on how to install `matlabengine`, the MATLAB API for Python, can be found here:

https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

You'll also need CPLEX, and the CPLEX API for Python (CPLEX is the ILP solver):

https://www.ibm.com/academic/topic/data-science?ach_id=6fe17098-43df-4a9d-8412-3377286841a3

https://www.ibm.com/docs/en/icos/20.1.0?topic=cplex-setting-up-python-api


Also, as of September 2022, Python 3.9.x is the newest Python version supported by CPLEX so don't use anything newer than that.
 

Finally, you can install all required Python packages by using:

```bash
pip install -r requirements.txt
```

## Usage

Browse through the source code. Most of the time, you'll want to run `generator/populate_solutions_dir.py` or `solver/gui.py`.

Have fun!

## Additional: `generator` design decisions

CPLEX is a lightning-fast ILP solver. It's used in this project because the authors of the paper (see [Credits](#credits)) used it. 

CPLEX is usually multithreaded, which is great, but the thing that's not so great is that the multithreaded mode works only when you want to output all the solutions CPLEX found in a single **.sol** file. The **.sol** solution files get really big (several GBs) when you increase the number of solutions you ask of CPLEX to find.

The natural way to deal with this problem is to split the process into batches, that is, to first find some number of solutions (let's say 1000), save them to a reasonably-sized *.sol file, and rinse and repeat. The problem with this is that since CPLEX treats this as an [MIP problem](https://www.ibm.com/docs/en/icos/20.1.0?topic=mip-stating-problem), it can't save the final state of execution and start from there the next time. That is, if you were to try to find all of the solutions by batching into sets of 1000 solutions, [CPLEX would just keep finding the same 1000 solutions](https://www.ibm.com/support/pages/stop-cplex-optimization-run-and-resume-it-later-time).

So the only reasonable thing that I could think of was to give up on multithreading, and use [IncumbentCallback](https://www.ibm.com/docs/en/icos/12.8.0.0?topic=SSSA5P_12.8.0/ilog.odms.cplex.help/refpythoncplex/html/cplex.callbacks.IncumbentCallback-class.html) to check if the solution is unique and save it, if it is.

