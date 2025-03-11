# run in the command line: $ mpiexec -n 4 python mpi_sum.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Each process uses the same predefined vector
local_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=int)

total_sum = np.zeros(1, dtype=int)
comm.Reduce(local_array, total_sum, op=MPI.SUM, root=0)  # Reduce with sum operation

# Print the result from rank 0
if rank == 0:
    print(f"Total sum of vectors: {total_sum}")