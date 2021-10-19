import os 
import stat 
import glob

from models.lo import LearningObject as los


def reapLos(LearningObject):
    for 'course' in LearningObject:
        Course = reapLoType('course')
        return Course

    for 'unit' in LearningObject:
        Unit = reapLoType('unit')
        return Unit

    for 'talk' in LearningObject:
        Talk = reapLoType('talk')
        return Talk

    for 'book' in LearningObject:
        Lab = reapLoType('book')
        return Lab

    for 'video' in LearningObject:
        Video = reapLoType('video')
        return Video

    for 'panelvideo' in LearningObject:
        PanelVideo = reapLoType('panelvideo')
        return PanelVideo

    for 'paneltalk' in LearningObject:
        PanelTalk = reapLoType('paneltalk')
        return PanelTalk

    for 'archive' in LearningObject:
        Archive = reapLoType('archive')
        return Archive

    for 'github' in LearningObject:
        Git = reapLoType('github')
        return Git

    for 'web' in LearningObject:
        Web = reapLoType('web')
        return Web
    
    return los
    
def reapLoType(pattern, parent, locreator):
    folders = glob.sync(pattern).sort()
    for folder in folders:
        if (os.path.isdir(stat.S_IFLNK(folder))):
            os.chdir(folder)
            lo = locreator(parent)
            los.append(lo)
            os.chdir('..')

    return los

def findTopLos(los, lotype):
