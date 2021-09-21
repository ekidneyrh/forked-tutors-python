from abc import ABC, abstractmethod
from pathlib import Path as fs

class LearningObject (ABC) :

    def __init__(self, parent = None):
        self.hide = False
        if self.parent:
            self.parent = parent
        self.lotype = "lo"

    def reap(pattern):
        pass

    @abstractmethod
    def publish(path):
        pass

