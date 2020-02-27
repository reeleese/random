from __future__ import print_function
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

while True:
        if rank == 0:
                # Get value
                print("Enter a positive integer (or negative to exit): ")
                value = input()
                print("Process {0} got value {1}".format(rank, value))

                # Commit suiceide and direct children to do the same via a game of telephone
	        if value < 0:
                        for node in xrange(1,size):
                                comm.send(value, dest=node, tag=11)
                        print("Process {0} exiting...".format(rank))
                        MPI.Finalize()
                        sys.exit(0)

                # Send value to node 1
                req = comm.send(value, dest=rank+1, tag=11)

                # Print data for each node
                for node in xrange(1, size):
                        to_print = comm.recv(source=node, tag=13)
                        print(to_print)

                # Recieve loop-back signal
                comm.recv(source=size-1, tag=12)
        else:
                # Receive value from previous node
                value = comm.recv(source=MPI.ANY_SOURCE, tag=11)
                if value < 0:
                        print("Process {0} exiting...".format(rank))
                        MPI.Finalize()
                        sys.exit(0)

                # Send print job to master (so things print in order)
                to_print = "Process {0} got value {1}".format(rank, value)
                comm.send(to_print, dest=0, tag=13)

                # Continue telephone game
                if rank == size-1:
                        comm.send(42069, dest=0, tag=12)
                else:
                        comm.send(value, dest=rank+1, tag=11)
