from abc import ABC, abstractmethod
import os
import yaml
import logging
import importlib.metadata as fm

class LearningObject (ABC) :

    lotype = "lo"

    def __init__(self):
        self.hide = False

    def reap(self, pattern):
        contents = dict()
        self.folder = os.path.basename(os.getcwd)
        self.parentFolder = getParentFolder()
        self.img = getImageFile(pattern)
        if os.path.exists('properties.yaml'):
            self.properties = readYaml('properties.yaml')
        if os.path.exists(pattern + '.md'):
            contents = fm(readWholeFile(pattern + '.md'))
            if contents.keys().len > 0 :
                self.frontMatter = contents
        self.title = getHeaderFromBody(contents)        


    @abstractmethod
    def publish(path):
        pass