class Fish:
    def __init__(self):
        ''' Constructor for this class.'''
        # Create some member animals
        self.members = ['Pike','Shark','Cod']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % member)
            
    def dangerous(self):
        self.members = ['Shark']