from abc import ABC, abstractmethod
import fileinput
import os
import yaml
import logging

class LearningObject (ABC) :

    lotype = "lo"

    def __init__(self):
        self.hide = False

    def reap(pattern):
        pass

    @abstractmethod
    def publish(path):
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
        header = array[0].substring(1)
    else:
        header = array[0]
    return header           
