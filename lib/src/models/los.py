import os
import glob
from abc import ABC, abstractmethod
from lib.src.models.lo import LearningObject
import utils.futils as futils
import utils.loutils as loutils
import lo

class DiscreteLearningObject(LearningObject):
    def __init__(self, parent):
        super().__init__(parent)

    def reap(self, pattern):
        pass

    def publish(path):
        pass

class Talk(DiscreteLearningObject):
    pass

class PanelTalk(DiscreteLearningObject):
    pass

class Archive(DiscreteLearningObject):
    pass