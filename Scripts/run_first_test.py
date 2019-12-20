import os
import get_filenames as gf
import set_xml as sxml
import get_command as gcom
import manage_dir as mdir
import generate_qsub_command as qcom


def GetXml(master_xml, xml_filename, this_bin, eCM):


    master = open(master_xml).read()
    copy = master

    copy = sxml.SetXmlParam( 'Eloss',copy,'maxT', 250 )
    copy = sxml.SetXmlParam( 'PythiaGun',copy,'pTHatMin', this_bin[0] )
    copy = sxml.SetXmlParam( 'PythiaGun',copy,'pTHatMax', this_bin[1] )
    copy = sxml.SetXmlParam( 'PythiaGun',copy,'eCM', eCM )
    copy = sxml.SetXmlParam( 'JetHadronization',copy,'eCMforHadronization', eCM )

    xml_file = open(xml_filename,'w')
    xml_file.write(copy)
    xml_file.close
    
    print(xml_filename+' is created')



def Submit(argc,argvs,code_path,this_bin,run):

    script_dir = os.getcwd()
    print('run '+str(run))
    eCM = int(argvs[1])

    outdir = '/wsu/tmp/AAPaper/PPTest'    
    #outdir = '/Users/yasukitachibana/Dropbox/Codes/AAPaperMGR/Test'
    master_xml = '../XmlMaster/first_test_matter_vacuum.xml'
    exec_name = 'FirstTestMatterVacuum'

    xml_filename = os.path.join(outdir,gf.GetXmlFilename(this_bin,run))
    sigma_filename = os.path.join(outdir,gf.GetSigmaFilename(this_bin,run))
    hadron_filename = os.path.join(outdir,gf.GetHadronListFilename(this_bin,run))
    out_filename = os.path.join(outdir,gf.GetTestOutFilename(this_bin,run))
    build_dir = os.path.join(outdir,gf.GetBuidDirName(this_bin,run))

    GetXml(master_xml, xml_filename, this_bin, eCM)

    command = gcom.GetCommand(code_path, build_dir, exec_name, xml_filename, out_filename, sigma_filename, hadron_filename)

    mdir.Mkdirs(build_dir)

    command_run = '"python run.py '+command+'"'

    master_command = os.path.join(script_dir,'JobMaster')+' '+script_dir+' '+command_run
    print(master_command)

    qsub_command = qcom.GenerateQsubCommand(gf.GetJobName(this_bin,run),master_command)

    print(master_command)
    #os.system(master_command)
    exit()
    
    print(qsub_command)
    os.system(qsub_command)


    

    
