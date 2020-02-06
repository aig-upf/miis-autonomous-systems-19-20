
# Autonomous Systems - Lab 2

# Installing a SAT solver

You can install any of the SAT solvers available from the SAT competitions 
<http://www.satcompetition.org/>.
An easier alternative might be to use [Minisat](http://minisat.se/), a 
minimalistic but very efficient SAT solver. Under Ubuntu, you can install it
with:

    sudo apt install minisat

# Getting started with the coding

Clone this repository:

    git clone https://github.com/aig-upf/miis-autonomous-systems-19-20.git
    cd miis-autonomous-systems-19-20/lab2
    
You will see some Python code to get you started. 
It basically will handle command-line arguments for you, parse Sudoku boards
into a more meaningful matrix-like representation, write files in the 
DIMACS CNF format, and parse the output of the SAT solver.
The code assumes you are using Minisat,
but should be easy to modify it if you choose another solver. 
Look at the `sudoku.py` and `utils.py` files in the `lab2` directory.
You're not required to use any of this code for your submission,
but it might help you focus on the interesting parts. 

