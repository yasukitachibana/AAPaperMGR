## get_filenames.py


def GetSigmaFilename(this_bin,run):
    return 'SigmaHardBin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)+'.out'

def GetHadronListFilename(this_bin,run):
    return 'JetscapeHadronListBin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)+'.out'

def GetTestOutFilename(this_bin,run):
    return 'TestOutBin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)+'.out'

def GetXmlFilename(this_bin,run):
    return 'SettingsBin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)+'.xml'

def GetBuidDirName(this_bin,run):
    return 'BuildBin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)

def GetJobName(this_bin,run):
    return 'Bin'+str(this_bin[0])+'_'+str(this_bin[1])+'_Run'+str(run)
