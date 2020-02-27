## run_jetscape_master

import sys
import get_pthat_bins as gpt
import setup as setup


def Main(argc,argvs):
    eCM = int(argvs[1])
    pthat_bins = gpt.GetPtHatBins( eCM )

    for this_bin in pthat_bins:
        print('pthat_bin: ', end='')
        print(this_bin, end=' (GeV)\n')
        #if this_bin[0] >= 2:
        run_total = 5
        for run in range(0,run_total):
            code_path = '/wsu/home/go/go54/go5410/JETSCAPE-COMP'
            setup.Submit(argc,argvs,code_path,this_bin,run)



def CheckArg(argc,argvs):

    if argc < 3:
        print('please input options')
        print('python run_jetscape_master.py [eCM] [PP/AA] [centrality, 0-10, 30-40, 30-40, 40-50] [alphaS] [Qs] [take_recoil 0 or 1]')
        exit()
    elif argvs[2] != 'PP' and  argc < 7:
        print('please input options')
        print('python run_jetscape_master.py [eCM] [PP/AA] [centrality, 0-10, 30-40, 30-40, 40-50] [alphaS] [Qs] [take_recoil 0 or 1]')
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
