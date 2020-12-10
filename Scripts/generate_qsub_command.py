import os

def GenerateQsubCommand(job_name,job_command):

    #head = 'sbatch --time=3:00:00 -p $SPRIMARY  --mem=32G'
    
    #head = 'sbatch --time=120:00:00 -p $SPRIMARY --mem=64G'
    #head = 'sbatch --time=72:00:00 -q secondary --mem=32G'

    #head = 'sbatch --time=720:00:00 -q secondary --mem=8G'
    head = 'sbatch --time=720:00:00 -q primary --mem=8G'
    #head = 'sbatch --time=72:00:00 -q secondary --mem=32G'
    #head = 'sbatch --time=72:00:00 -q primary --mem=32G'

    #head = 'sbatch --time=72:00:00 -p $SPRIMARY --mem=8G'
    #head = 'sbatch --time=62:00:00 -p $SPRIMARY --mem=8G'
    #head = 'sbatch --time=72:00:00 -q requeue --mem=16G'
    

    #head = 'qsub -V -q eamxq -l mem=16gb -l cpu_type=Intel  '
    #head = 'qsub -V -q mwsuq -l mem=32gb -l cpu_type=Intel  '
    #head = 'qsub -V -q mwsuq -l mem=16gb -l cpu_type=Intel  '
    #head = 'qsub -V -q eamxq -l mem=32gb -l cpu_type=Intel  '
    #head = 'qsub -V -q eamxq -l mem=24gb -l cpu_type=Intel  '
    #head = 'qsub -V -q wsuq -l mem=24gb -l ncpus=4 -l cpu_type=Intel  '
    #head = 'qsub -V -q wsuq -l mem=16gb -l cpu_type=Intel'
    #head = 'qsub -V -q wsuq -l mem=32gb -l cpu_type=Intel'
    #head = 'qsub -V -q eamxq -l mem=32gb -l ncpus=8 -l cpu_type=Intel  '
    #head = 'qsub -V -q mwsuq -l mem=24gb -l ncpus=4 -l cpu_type=Intel  '
    #head = 'qsub -V -q eamxq -l mem=24gb -l ncpus=4 -l cpu_type=Intel  '
    out = "/dev/null"
    error =  "/dev/null"
    #log = '-N {} -o {} -e {}  -- '.format(job_name,out,error)
    log = '--job-name={} -o {} -e {} '.format(job_name,out,error)
    return head+' '+log+' '+job_command
