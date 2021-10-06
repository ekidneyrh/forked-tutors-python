from abc import ABC, abstractmethod
from pathlib import Path as path
import fnmatch as fn
import os

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
    for type in validImageTypes:
        image = name + '.' + type
        if os.path.exists(image):
            return image
    