from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size() #get the total number of processes

if size < 2:
    print("At least two processes are required to run this program.")
else:
    if rank == 0:
        data= {'Key1':  'value1', 'Key2': 'value2'}
        comm.send(data, dest=1) #send data to  process with rank 1
        print("Sent data from process 0")
        
    elif rank == 1:
        data = comm.recv(source=0) #receive data from process with rank 1
        print("Received data at process 1: {data}")#print the received data
    
    else:
        print("The Process {rank} is idle") #print a message for idle processes
        

