from abc import ABCMeta, abstractmethod
'''
Factory method

'''

# I am the product interface
class Section(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def describe(self):
        pass


# These are the concrete product classes
class PersonalSection(Section):
    def describe(self):
        print 'Personal Info'


class AlbumSection(Section):
    def describe(self):
        print 'Personal Album'


class PatentSection(Section):
    def describe(self):
        print 'My patents'


class PublicationSection(Section):
    def describe(self):
        print 'Publications'

# This is the creator
class Profile(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


#This part is the concrete creator
class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(AlbumSection)


class Linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(PatentSection)
        self.addSections(PublicationSection)


if __name__ == '__main__':
    profile_type = input("Which profile do you want to create? [ Linkedin or"
                         " Facebook]")
    profile = profile_type()
    print ("Creating profile..", eval(type(profile).__name__))
    print("Profile has section --", profile.getSections())
    profile.sections[0]().describe()
