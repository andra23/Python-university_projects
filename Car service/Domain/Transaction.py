import datetime
class Transaction():
    """
        Transaction business object.
    """
    def __init__(self,id,idCar,idCard,sumaP,sumaM,date,hour,delete=None):
        '''
        Creates a transaction.
        :param id:
        :param idCar:
        :param idCard:
        :param sumaP:
        :param sumaM:
        :param date:
        :param hour:
        '''
        self.__delete=delete
        self.__id = id
        self.__idCar = idCar
        self.__idCard = idCard
        self.__sumaP = sumaP
        self.__sumaM = sumaM
        try:
            self.__date = date
            datetime.datetime.strptime(date, '%d.%m.%Y')

        except ValueError:
            raise ValueError ("Incorrect data format, should be DD.MM.YYYY")
        self.__hour = hour

    def getCarDel(self):
        return self.__delete

    def setCarDel(self, newdel):
        self.__delete = newdel

    def getTId(self):
        return self.__id

    def setTId(self, newId):
        self.__id =int(newId)

    def getIdCar(self):
        return self.__idCar

    def setIdCar(self, newIdCar):
        self.__idCar = int(newIdCar)

    def getIdCard(self):
        return self.__idCard

    def setIdCard(self, newIdCard):
        self.__idCard = int(newIdCard)

    def getSumaP(self):
        return self.__sumaP

    def setSumaP(self, newSumaP):
        self.__sumaP = float(newSumaP)

    def getSumaM(self):
        return self.__sumaM

    def setSumaM(self, newSumaM):
        self.__sumaM =float( newSumaM)

    def getDate(self):
        return self.__date

    def setDate(self, newDate):
        self.__date = newDate

    def getHour(self):
        return self.__hour

    def setHour(self, newHour):
        self.__hour = float(newHour)

    def __str__(self) -> str:
        return "Transaction Id: {0}; Car Id: {1}; Card Id: {2}; Suma piese: {3}; Suma manopera: {4}; Date:{5}; Hour: {6}; "": {7} ".format(
            self.getTId(),
            self.getIdCar(),
            self.getIdCard(),
            self.getSumaP(),
            self.getSumaM(),
            self.getDate(),
            self.getHour(),
            self.getCarDel()
        )

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False
        return self.getTId() == other.getTId() and\
               self.getIdCar() == other.getIdCar() and\
               self.getIdCard() == other.getIdCard() and \
               self.getSumaP() == other.getSumaP() and\
               self.getSumaM() == other.getSumaM() and\
               self.getDate() == other.getDate() and\
               self.getHour() == other.getHour()

    def __ne__(self, other):
        return not (self == other)
