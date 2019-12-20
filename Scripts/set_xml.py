import re
import os

def SetXmlParam(module_name,copy,tag,val):
    
    tag_module = GetTag(module_name)
    match = re.search(tag_module,copy)
    org = ''
    if match:
        org = match.group()
    else:
        print('failed to find the tag for the module: ' + module_name)
        exit()

    new = org
    new = re.sub(GetTag(tag),GetTagVal(tag,val),new)
    return copy.replace(org,new)


def GetTag(tag):
    return '<'+tag+'>(.|\s)*?</'+tag+'>'

def GetTagVal(tag,val):
    message1 = '\t<!-- auto-generated  -->\n\t'
    message2 = '\n\t<!-- --------------- -->'
    return message1+'<'+tag+'>'+str(val)+'</'+tag+'>'+message2


