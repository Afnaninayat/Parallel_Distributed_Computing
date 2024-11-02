import multiprocessing

def child_process(pipe):
    
    pipe[1].close()
    
    
    data = pipe[0].recv()  
    print(f"Child process received data: {data}")
    
    
    pipe[0].close()

if __name__ == '__main__':
    
    pipe = multiprocessing.Pipe()

    
    process = multiprocessing.Process(target=child_process, args=(pipe,))
    process.start()

    
    pipe[0].close()

    
    message = "Hello from the parent process!"
    pipe[1].send(message)
    print("Parent process sent data.")

    
    pipe[1].close()

    
    process.join()