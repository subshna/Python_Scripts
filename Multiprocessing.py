from multiprocessing import Process
import os, math

def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

    processes = []

    for i in range(os.cpu_count()):
        print ('Registering Processes %d' %i)
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()