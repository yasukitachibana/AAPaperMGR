## run_jetscape_master

import sys
import get_pthat_bins as gpt
import run_first_test as ftest


def Main(argc,argvs):
    eCM = int(argvs[1])
    pthat_bins = gpt.GetPtHatBins( eCM )

    for this_bin in pthat_bins:
        print('pthat_bin: ', end='')
        print(this_bin, end=' (GeV)\n')

        run_total = 5
        for run in range(0,run_total):
            code_path = '/Users/yasukitachibana/Dropbox/Codes/JETSCAPE-COMP'
            ftest.Submit(argc,argvs,code_path,this_bin,run)
    


def CheckArg(argc,argvs):
    if argc < 2:
        print('please input options')
        print('python run_jetscape_master.py [eCM] [PP/AA]')
        exit()
    else:
        
        print( 'system: '+argvs[2] )
        if int(argvs[1]) != 5020 or argvs[2] != 'PP':
            exit()


        
if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    CheckArg(argc,argvs)
    Main(argc,argvs)
