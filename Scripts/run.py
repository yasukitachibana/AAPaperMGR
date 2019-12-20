import os
import sys
import shutil

import numpy as np
import subprocess

def Main(argc,argvs):

    #---------------------------------------
    job_command = ''
    for i in range(1,argc):
        job_command += argvs[i] + ' '
    #print(job_command)
    os.system(job_command)
    #---------------------------------------



if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    Main(argc,argvs)

