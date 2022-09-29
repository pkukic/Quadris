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

I consider this project mostly finished. On my machine (Ryzen 7 4700u, 24 GB RAM) `populate_solutions_dir` can find a new, **unique** solution of the board about every 1 - 3 seconds (I only ran it for 40k solutions, so 3 seconds per solve was the worst I got). Also, `gui.py` can find a solution to a partially solved board in less than 5 seconds. 

## TODO:  Requirements

### TODO: Document CPLEX/SQLITE