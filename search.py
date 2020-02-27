from __future__ import print_function

from mpi4py import MPI
import numpy as np
import sys
import os

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() #identifies the rank(id) of process, Master always is 0
size = comm.Get_size() #number of proccesses specified when running your program -n switch

# Objects local to each node
sendArr = None
chunkSize = None

if rank == 0: #if master
    # Check we got a file
    #if len(sys.argv) != 2:
     #   sys.exit(1)

    # Build Array and scatter
    sendArr = np.loadtxt(sys.argv[1], dtype='i')
    sendArr = sendArr.reshape(size, sendArr.shape[0] // size)
    chunkSize = sendArr.shape[1]

# Give each node a chunk
chunkSize = comm.bcast(chunkSize, root=0)
recvArr = np.empty(chunkSize, dtype='i')
comm.Scatter(sendArr, recvArr, root=0)

index = np.zeros(1)
request = comm.Irecv(index, source=MPI.ANY_SOURCE, tag=12) #receives this signal if othe rprocess found 11
for i in range(chunkSize):
    # See if found
    if request.Test() or i == chunkSize - 1:
        print("Process {0} stopped searching at index {1}".format(rank, i))
        sys.exit(0)

    # Found it
    if recvArr[i] == 11:
        for proc in range(1,size):
            index = np.array([i])
            comm.Isend(index, dest=proc, tag=12)
            lineNumber = rank * chunkSize + i
            print("The magic number 11 was found at index %d (line %d) by process %d.\n" % (index[0], lineNumber, rank))
            sys.exit(0)

