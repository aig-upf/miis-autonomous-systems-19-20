import subprocess
import time


def parse_minisat_output(filename):
    with open(filename, 'r') as f:
        result = f.readline().rstrip('\n')
        if result != 'SAT':
            return result, {}
        model = f.readline().rstrip('\n')
        lits = (int(x) for x in model.split(' '))
        sat_assignment = {abs(x): x > 0 for x in lits}
        return result, sat_assignment


def solve(cnf_filename, verbose):
    """ Invoke the Minisat solver on the given file in DIMACS CNF format.
    Return a tuple <res, assignment>, where res is either "SAT" or "UNSAT",
    and assignment is a dictionary mapping variable indexes to their truth values in
    a satisfying assignment, if SAT, or an empty dictionary, otherwise.
    """
    output = 'solver.output'
    cmd = ['minisat', cnf_filename, output]

    if verbose:
        retcode = subprocess.call(cmd)
    else:  # Redirect the output
        with open('solver.log', 'w') as stdout:
            with open('solver.err', 'w') as stderr:
                retcode = subprocess.call(cmd, stdout=stdout, stderr=stderr)

    return parse_minisat_output(output)


def save_dimacs_cnf(variables, clauses, filename, verbose):
    numvars = len(variables)
    numclauses = len(clauses)

    if verbose:
        print(f'Writing SAT problem with {numvars} vars and {numclauses} clauses to file "{filename}"')

    with open(filename, "w") as output:
        print("c CNF encoding generated on {}".format(time.strftime("%Y%m%d %H:%M:%S", time.localtime())), file=output)
        print(f"p cnf {numvars} {numclauses}", file=output)  # p cnf nbvar nbclauses
        for clause in clauses:
            print(print_clause(clause), file=output)


def print_clause(literals):
    return " ".join(map(str, literals)) + " 0"  # Dimacs clauses are lines ending with a 0
