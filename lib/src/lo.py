from abc import ABC, abstractmethod
from pathlib import Path as path

class LearningObject (ABC) :

    def __init__(self):
        self.hide = False
        self.lotype = "lo"

    def reap(pattern):
        pass

    @abstractmethod
    def publish(path):
        pass

