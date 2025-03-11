# run in the command line: $ mpiexec -n 4 python mpi_ranks.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("Rank of the process: ",rank)