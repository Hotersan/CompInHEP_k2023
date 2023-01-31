#!/usr/bin/env python

from multiprocessing import Process
import os

n=10

def hello(mpn):
    st='./hw.out %s'%mpn+' > OneB/job%s'%mpn+'_'+str(os.getpid())+'_'+str(os.getppid())
    os.system(st)

for i in range(n):
    p = Process(target=hello, args={i+1,})
    p.start()
