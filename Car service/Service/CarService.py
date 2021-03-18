from Domain.Car import Car
import datetime
from Domain.Transaction import Transaction
fileName="masini.txt"
import json
class CarService():
    '''
    Manages car logic
    '''
    def __init__(self, repo,transactionService):
        """
        Creates a car service.
        """

        self.__repo = repo
        self.__transactionService=transactionService

    def add_car(self,idCar,model,year,NoKm,guarantee):
       '''
       Creates and add a car in the cars list.
       :param idCar: int, the car id
       :param model: str, the car model
       :param year: int, the year of acquisition
       :param NoKm: float, the number of km
       :param guarantee: str, in guarantee-yes/no
       :return: 
       '''
       errors = []

       if idCar in self.__repo.getAll():
           errors.append('Exista deja o masina cu id-ul []'.format(idCar))
       if year<=0:
           errors.append('Anul fabricatiei trebuie sa fie strict pozitiv!')
       if NoKm<0:
           errors.append('Numarul de km trebuie sa fie strict poztiv!')
       if guarantee not in ["da","nu"]:
           errors.append("Garantia trebuie sa fie una dintre:da,nu.")
       if errors != []:
           raise ValueError(errors)
       car = Car(idCar,model,year,NoKm,guarantee)
       #self.__repo.addCar(self,car)
       self.__repo.addCar(car)


    def get_all(self):
        """
        :return: a list of all the cars.
        """
        return self.__repo.getAll()

    def remove_car(self,car):

        '''   errors=[]
        if car not in self.__carsList:
            errors.append("Masina nu exista in lista!")
        if errors!=[]:
            raise ValueError(errors)
        '''
        self.__repo.removeCar(car)
    def remove_car1(self,car):

        '''   errors=[]
        if car not in self.__carsList:
            errors.append("Masina nu exista in lista!")
        if errors!=[]:
            raise ValueError(errors)
        '''
        self.__repo.removeCar1(car)

    def update_car(self,id,newId,newModel,newYear,newNoKm,newGuarantee):
        '''
        Modifica o masina care se identifica dupa un id dat de la tastatura.
        :param id: id -ul masinii-int
        :param carsList: lista de masini-list
        :param newId: -noul id-int
        :param newModel: -noul model-str
        :param newYear: -noul an de fabricatie-int
        :param newNoKm: -noul numar de km-float
        :param newGuarantee: -noua garantie-da/nu-str
        :return:
        '''
        self.__repo.updateCar(id,newId,newModel,newYear,newNoKm,newGuarantee)

    def search_car(self,caract,word):
        '''
        Cauta masina in functie de (model,an fabricatie,nr.km,garantie)
        :param caract: -categoria dupa care se face cautarea-str
        :param word: -caracteristica masinii -poate fi str,int,float
        :return: -lista cu masinile care se incadreaza in cerintele de mai sus -list
        '''
        newList=[]
        carsList = self.__repo.getAll()
        for i in range (len(carsList)):
            car=carsList[i]
            if caract== "model":
                if car.getModel()==word:
                    newList.append(str(carsList[i]))
            elif caract=="an fabricatie":
                if car.getYear()==word:
                    newList.append(str(carsList[i]))
            elif caract=="nr.km":
                if car.getNoKm()==word:
                    newList.append(str(carsList[i]))
            elif caract=="garantie":
                if car.getGuarantee()==word:
                    newList.append(str(carsList[i]))
        return newList
    def order_car_desc(self):
        '''
        Ordoneaza masinile descrescator dupa suma obtinuta pe manopera.
        :return: -lista ordonata  cu masini-list
        '''
        lista=[]
        newlist=[]
        lista1=[]
        tranList=self.__transactionService.getAll()
        carsList=self.__repo.getAll()
        for tran in tranList:
            lista.append(tran.getSumaM())
            lista.sort(reverse=True)
        for i in range(len(lista)):
            for tran in tranList:
                if lista[i]==tran.getSumaM():
                    lista1.append(tran.getIdCar())
        for i in range(len(lista1)):
            for j in range(len(carsList)):
                car=carsList[j]
                if lista1[i]==int(car.getCarId()):
                    newlist.append(str(car))
        string = str(newlist[:])
        comp = string.split(",")
        return comp
    def update_cars_garantie(self):
        '''
        Actualizaza garantiile masinilor care au mai mult de 3 ani de la data fabricatiei si peste 60000km.
        :return: -
        '''
        carsList=self.__repo.getAll()
        now = datetime.datetime.now()
        currentYear=now.year
        for car in carsList:
            year=int(car.getYear())
            km=int(car.getNoKm())
            if (currentYear-year)>3 or km>60000:
                car.setGuarantee("nu")
        self.__repo.writeToFile()























