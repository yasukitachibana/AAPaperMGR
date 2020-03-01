import os
import get_filenames as gf
import set_xml as sxml
import get_command as gcom
import manage_dir as mdir
import generate_qsub_command as qcom
import set_path as spath
import glob as glob
import shutil



def Check(argc,argvs,code_path,this_bin,run):

    resub = 0
    
    script_dir = os.getcwd()
    print('run '+str(run))
    eCM = int(argvs[1])
    PPAA = argvs[2]
    
    outdir = os.path.join(spath.GetOutputPath(),gf.GetOutdirname(argc,argvs))
    if not os.path.isdir(outdir):
        print(outdir, ' does not exist. Exit.')
        exit()
        
    out_filename = os.path.join(outdir,gf.GetTestOutFilename(this_bin,run))
    
    event_num = 0
    
    if os.path.exists(out_filename):
        with open(out_filename, mode='r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            lines = [line for line in lines if 'Event' in line]
            lines = [line for line in lines if not 'EventPlaneAngle' in line]
            event_num = int(lines.split()[0])
            print(out_filename, ' exists. final event number = ', event_num)
    else:
        print(out_filename, ' does not exist.')
    
    if not event_num == (4000-1):
        resub = 1
        build_dir = os.path.join(outdir,gf.GetBuidDirName(this_bin,run))
        if os.path.isdir(build_dir):
            if not mdir.IsEmpty(build_dir):
                shutil.rmtree(build_dir)
    
    return resub





