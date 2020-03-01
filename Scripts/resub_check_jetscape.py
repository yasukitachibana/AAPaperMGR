## resubmit_jetscape_master

import sys
import get_pthat_bins as gpt
import setup as setup
import set_path as spath
import check_results as cres
import os
import get_filenames as gf
import generate_qsub_command as qcom

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
            
            print('run '+str(run))
            eCM = int(argvs[1])
            PPAA = argvs[2]
            
            outdir = os.path.join(spath.GetOutputPath(),gf.GetOutdirname(argc,argvs))
            if not os.path.isdir(outdir):
                print(outdir, ' does not exist. Exit.')
                #exit()
            out_filename = os.path.join(outdir,gf.GetTestOutFilename(this_bin,run))
            print('Seeing inside of ' + out_filename)
            
            script_dir = os.getcwd()
            command = 'python check_results.py ' + out_filename
            
            master_command = os.path.join(script_dir,'JobMaster')+' '+script_dir+' "'+command+'"'
            qsub_command = qcom.GenerateQsubCommand('c'+gf.GetJobName(this_bin,run),master_command)
            print('Submission, Qsub Command')
            print(qsub_command)
            print('-')
            #os.system(qsub_command)

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
    print( 'Check the status of runs for the setting with' )
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
