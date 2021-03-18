import json
fileName="masini.txt"
class Car():
    """
        Car business object.
    """
    def __init__(self,idCar,model,year,noKm,guarantee,delete=None):
        '''
        Creates a car.
        :param idCar: int, the car id
        :param model: str, the car model
        :param year: int, the year of acquisition
        :param noKm: int, the number of km
        :param guarantee: str, in guarantee-yes/no
        '''
        self.__delete=delete
        self.__idCar=idCar
        self.__model=model
        if year>0:
            self.__year=year
        else:
            raise ValueError("The year should be a strictly positive number!")
        if noKm>=0:
            self.__noKm=noKm
        else:
            raise ValueError("NoKm should be a positive number!")
        self.__guarantee=guarantee
    def getCarDel(self):
        return self.__delete

    def setCarDel(self,newdel):
        self.__delete=newdel

    def getCarId(self):
        return self.__idCar

    def setId(self,newId):
        self.__idCar=int(newId)

    def getModel(self):
        return self.__model

    def setModel(self,newModel):
        self.__model=newModel

    def getYear(self):
        return self.__year

    def setYear(self,newYear):
        if int(newYear)<0:
            raise ValueError("Not negative!")
        self.__year=int(newYear)

    def getNoKm(self):
        return self.__noKm

    def setNoKm(self,newKm):
        if int(newKm)<0:
            raise ValueError("Not negative!")
        self.__noKm=float(newKm)

    def getGuarantee(self):
        return self.__guarantee

    def setGuarantee(self,newGuarantee):
        self.__guarantee=newGuarantee


    def __str__(self) -> str:
        return "Car Id: {0}; Model: {1}; Year: {2}; Number Km: {3}; In guarantee: {4}; " "{5}:  ".format(self.getCarId(),
                                                                                             self.getModel(),
                                                                                             self.getYear(),
                                                                                             self.getNoKm(),
                                                                                             self.getGuarantee(),
                                                                                             self.getCarDel())

    def __eq__(self, other):
        if not isinstance(other,Car):
            return False
        return self.getCarId()==other.getCarId() and \
               self.getModel()==other.getModel() and \
               self.getYear()==other.getYear() and \
               self.getNoKm()==other.getNoKm() and \
               self.getGuarantee()==other.getGuarantee()
    def __ne__(self, other):
        return not (self==other)



