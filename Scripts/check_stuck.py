## run_jetscape_master

import sys
import get_pthat_bins as gpt
import setup as setup
import set_path as spath
import os
import datetime
import time


def Main(argc,argvs):

    print( '###############')
    print( 'Search Output file without having any updates within 3 hours')
    print( '###############')


    code_path = spath.GetCodePath()
    print('Code Path:', code_path)
    eCM = int(argvs[1])
    pthat_bins = gpt.GetPtHatBins( eCM )

    import glob
    files = glob.glob('*')
    
    for file in files:
        s = os.path.getmtime(file)
        d = datetime.datetime.fromtimestamp(s)
        print(d, s)
        
        genzai = time.time()

        genzai2 = datetime.datetime.fromtimestamp(genzai)


        delta_t = abs(genzai2 - d)
        
        if delta_t.total_seconds() > GetSeconds(3.0):
            print(genzai)
            print(genzai2)
            print(delta_t.total_seconds())
        

    #for this_bin in pthat_bins:
#        print('pthat_bin: ', end='')
#        print(this_bin, end=' (GeV)\n')
#        #if this_bin[0] <= 9:
#        #    continue
#        #run_total = 10
#        #for run in range(0,run_total):
#        for run in range(20,25):
#            setup.Submit(argc,argvs,code_path,this_bin,run)


def GetSeconds(hours):
    minutes = hours*60.0
    seconds = minutes*60.0
    return seconds

def CheckArg(argc,argvs):

    if argc < 3:
        print('please input options')
        print('python run_jetscape_master.py [eCM] [PP/AA] [centrality, 0-10, 30-40, 40-50] [alphaS] [Qs] [take_recoil 0 or 1]')
        exit()
    elif argvs[2] != 'PP' and  argc < 7:
        print('please input options')
        print('python run_jetscape_master.py [eCM] [PP/AA] [centrality, 0-10, 30-40, 40-50] [alphaS] [Qs] [take_recoil 0 or 1]')
        exit()

    print( '###############')
    print( '###############')
    print( 'eCM: '+argvs[1] )
    print( 'system: '+argvs[2] )
    if argvs[2] != 'PP':
        print( 'centrality: '+argvs[3] )
        print( 'alphaS: '+argvs[4] )
        print( 'Qs: '+argvs[5] )
        no_yes = ['No','Yes']
        print( 'take recoil: '+no_yes[int(argvs[6])] )
    print( '###############')
    print( '###############')
        
if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    CheckArg(argc,argvs)
    Main(argc,argvs)
