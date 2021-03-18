import datetime
class Card():
    """
        Car business object.
    """
    def __init__(self,id,name,fisrtName,CNP,dateB,dateR,delete=None):
        '''
        Creates a card.
        :param id: card id-int
        :param name: name -str
        :param fisrtName: -str
        :param CNP: -int
        :param dateB: str (dd.mm.yy)
        :param dateR: str
        '''
        self.__delete=delete
        self.__id = id
        self.__name = name
        self.__firstName = fisrtName
        self.__CNP=CNP
        try:
            self.__dateB = dateB
            datetime.datetime.strptime(dateB,'%d.%m.%Y')

        except ValueError:
            raise ValueError ("Incorrect data format, should be DD.MM.YYYY")
        try:
            self.__dateR = dateR
            datetime.datetime.strptime(dateR,'%d.%m.%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD.MM.YYYY")

    def getCarDel(self):
        return self.__delete

    def setCarDel(self, newdel):
        self.__delete = newdel

    def getCardId(self):
        return self.__id

    def setId(self, newId):
        self.__id = int(newId)

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, newFirstName):
        self.__firstName = newFirstName

    def getCNP(self):
        return self.__CNP

    def setCNP(self,newCNP):
        self.__CNP = int(newCNP)
    def getDateB(self):
        return self.__dateB

    def setDateB(self, newDateB):
        self.__dateB = newDateB

    def getDateR(self):
        return self.__dateR

    def setDateR(self, newDateR):
        self.__dateR = newDateR

    def __str__(self) -> str:
        return "Card Id: {0}; Name: {1}; First Name: {2}; CNP: {3}; Date of birth: {4}; Date of registration: {5}; " ":{6}".format(
            self.getCardId(),
            self.getName(),
            self.getFirstName(),
            self.getCNP(),
            self.getDateB(),
            self.getDateR(),
            self.getCarDel()
        )

    def __eq__(self, other):
        if not isinstance(other,Card):
            return False
        return self.getCardId() == other.getCardId() and \
               self.getName() == other.getName() and \
               self.getFirstName() == other.getFirstName() and \
               self.getCNP() == other.getCNP() and \
               self.getDateB() == other.getDateB() and \
               self.getDateR() == other.getDateR()
    def __ne__(self, other):
        return not (self==other)
