from models.lo import LearningObject
from utils.properties import Properties
import utils.futils
import utils.loutils
import topic as Topic
import os
from abc import ABC, abstractmethod
 
class Course(LearningObject):
   def __init__(self):
       super().__init__()
 
   def insertCourseRef(los):
       for lo in los:
           lo.course = self
       if lo.course is Topic:
           self.insertCourseRef(lo.los)
       self.course = self;
