
# Autonomous Systems - Lab 2

# Installing PySMT and solvers

Clone this repository and install all the Python requirements:

    git clone https://github.com/aig-upf/miis-autonomous-systems-19-20.git
    cd miis-autonomous-systems-19-20/lab2
    pip install -r requirements.txt 
    

Install one or more of the (SMT) solvers that `pySMT` interfaces with.
SMT solvers can solve problems represented in an extension of pure
propositional logic, but of course they solve propositional problems
as well. You can install this easily with the `pysmt-install` tool that
the commands above will have installed on your machine. Run `pysmt-install -h`
for a list of available solvers. We suggest you try with `z3`, `msat` or `cvc4`: 

    pysmt-install --z3
    pysmt-install --msat
    pysmt-install --cvc4
    
Note that `pysmt-install` is just a script to make it easy for you to download
and compile the actual solvers. The script will expect that your system has some
standard packages to compile C++ / Python libraries. `z3` is perhaps the easiest
to install, as it requires little compilation, but if none of the above
commands work, try installing these packages before running the command,
e.g. in Ubuntu: 

    sudo apt install build-essential g++ make cmake flex bison libgmp3-dev swig

# Getting started with the coding

We have implemented a few lines of code to get you started. Look at the
`nqueens.py` file in the `lab2` directory.
The `utils.py` file also contains some routines that
you might find useful. You're not required to use any of this code for 
your submission, but might help you start. 

