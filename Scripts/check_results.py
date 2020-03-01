import os
import get_filenames as gf
import set_xml as sxml
import get_command as gcom
import manage_dir as mdir
import generate_qsub_command as qcom
import set_path as spath
import glob as glob
import shutil
import sys



def Main(argc,argvs):

    if argc < 2:
        exit()


    out_filename = argvs[1]
    
    event_num = 0
    
    if os.path.exists(out_filename):
        with open(out_filename, mode='r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            lines = [line for line in lines if 'Event' in line]
            lines = [line for line in lines if not 'EventPlaneAngle' in line]
            event_num = int(lines[-1].split()[0])
            print(out_filename, ' exists. final event number = ', event_num)
    else:
        print(out_filename, ' does not exist.')
    
    if not event_num == (4000-1):
        print('Incompleted. To be submitted again.')
   
        fname = os.path.basename(out_filename)
        sfname = 'Status'+fname

        status_filename = os.path.join(os.path.dirname(out_filename),sfname)
        print(status_filename)
        
        out_file = open(status_filename,'w')
        out_file.write('incompleted')
        out_file.close
        
        
        
        
    else:
        print('Good. To be Skipped.')
    


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    Main(argc,argvs)



