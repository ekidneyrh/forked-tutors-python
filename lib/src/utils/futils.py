import os
import logging
import yaml

def __init__(self):
    pass

def getImageFile(name):
    validImageTypes = ['png','jpg','jpeg','gif']
    image = ''
    for type in validImageTypes:
        image = name + '.' + type
        if os.path.exists(image):
            return image

def getParentFolder():
    return os.path.basename(os.path.dirname(os.getcwd)) 

def readYaml(path):
    yamldata = ''
    try:
        yamldata = yaml.load(os.open(path, encoding='utf-8'))
    except:
        logging.warning('Tutors ${version} encountered an error reading properties.yaml:')
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.mark.buffer)
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.message)
        logging.warning('Review this file and try again....')
    return yamldata

def readWholeFile(path):
    if os.path.exists(path):
        array = os.open(path)
        return array
    else:
        logging.warning('Unable to locate ' + path)

def getHeaderFromBody(body):
    array = body.split('\n')
    header = ''
    if array[0][0] == '#':
        header = array[0][0:2]
    else:
        header = array[0]
    return header           

def withoutHeaderFromBody(body):
    content = body
    line1 = content.index('\n')
    content = content[line1 + 1 : content.len()]
    content = content.strip()
    line2 = content.index('\n')
    if line2 > -1:
        content = content[0:line2]
    return content    