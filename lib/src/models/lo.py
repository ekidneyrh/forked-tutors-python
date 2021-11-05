from abc import ABC, abstractmethod
import os
import yaml
import logging
import utils.futils as futils
import frontmatter as fm

class LearningObject (ABC) :

    

    def __init__(self):
        self.hide = False
        self.lotype = "lo"
        
    def reap(self, pattern):
        contents = dict()
        self.folder = os.path.basename(os.getcwd)
        self.parentFolder = futils.getParentFolder()
        self.img = futils.getImageFile(pattern)
        if os.path.exists('properties.yaml'):
            self.properties = futils.readYaml('properties.yaml')
        if os.path.exists(pattern + '.md'):
            contents = fm.load(pattern + '.md')
            if contents.keys().len > 0 :
                self.frontMatter = contents
            self.title = futils.getHeaderFromBody(contents['body'])
            self.title = self.title + ' '
            self.objectivesMd = futils.withoutHeaderFromBody(contents['body'])    
        else:
            self.title = pattern
        self.videoids = futils.realVideoIds()
        self.videoid = self.videoids.videoid    


    @abstractmethod
    def publish(path):
        pass
