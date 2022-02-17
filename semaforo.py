#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:28:26 2022

@author: alumno
"""
from multiprocessing import Process, Value, BoundedSemaphore


def task(common, tid, semaforo):
    
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        semaforo.acquire()
        try:
            print(f'{tid}−{i}: Critical section')
            v = common.value + 1
            print(f'{tid}−{i}: Inside critical section')
            common.value = v
            print(f'{tid}−{i}: End of critical section')
        finally:
            semaforo.release()
        
           
def main(N, k=1):
    
    lp = []
    common = Value('i', 0)
    semaforo = BoundedSemaphore(k)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, semaforo)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")
        
        
if __name__ == "__main__":
    N = 8
    main(N)
        
        
        