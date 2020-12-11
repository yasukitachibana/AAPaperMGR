import os

def GetCodePath():
    return '/wsu/home/go/go54/go5410/JETSCAPE-COMP'

def HydroFilePath(centrality):
    dir = '/wsu/home/go/go54/go5410/maj-shen/JETSCAPEDataFile/HydroProfiles'
    return os.path.join(dir, '5TeV_'+centrality)

def GetOutputPath():
    #return '/wsu/tmp/AAPaper'
    #return '/wsu/tmp/AA_Tc_T0'
    return '/wsu/tmp/AA_200_200'
    #return '/wsu/tmp/AA_180_180'

def GetMasterXmlPath():
    return os.path.join(GetCodePath(),'examples/jetscape_init.xml')
