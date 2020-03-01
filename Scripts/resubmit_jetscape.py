## resubmit_jetscape_master

import sys
import get_pthat_bins as gpt
import setup as setup
import set_path as spath
import check_results as cres
import get_filenames as gf
import os
import manage_dir as mdir
import shutil


def Main(argc,argvs):
    code_path = spath.GetCodePath()
    print('Code Path:', code_path)
    eCM = int(argvs[1])
    pthat_bins = gpt.GetPtHatBins( eCM )

    for this_bin in pthat_bins:
        print('pthat_bin: ', end='')
        print(this_bin, end=' (GeV)\n')
        #if this_bin[0] >= 2:
        run_total = 5
        for run in range(0,run_total):
            outdir = os.path.join(spath.GetOutputPath(),gf.GetOutdirname(argc,argvs))
            out_filename = os.path.join(outdir,gf.GetTestOutFilename(this_bin,run))
            
            fname = os.path.basename(out_filename)
            sfname = 'Status'+fname

            status_filename = os.path.join(os.path.dirname(out_filename),sfname)
            print('Refering Status File: ' + status_filename)
            
            if os.path.exists(status_filename):
                print('Incompleted. To be resubmitted.')
                build_dir = os.path.join(outdir,gf.GetBuidDirName(this_bin,run))
                if os.path.isdir(build_dir):
                    if not mdir.IsEmpty(build_dir):
                        shutil.rmtree(build_dir)
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
