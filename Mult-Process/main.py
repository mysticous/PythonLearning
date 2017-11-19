import sys
import json
from multiprocessing import Process
import os
import requests
start = 120315
batch = 50
threads = 6
'''121315'''

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def proc(strt, bat, no=0):
    os.system('python spider.py ' + str(strt) + ' ' + str(batch) + ' ' + str(
        no))
    print(os.getpid(), 'Process {} finished.'.format(no))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    func = proc
    p = []
    for i in range(threads):
        p.append(Process(target=func, args=(start - i * batch, batch, i + 1)))
    print('Child process will start.')
    for i in range(threads):
        p[i].start()