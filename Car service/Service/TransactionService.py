from Domain.Transaction import Transaction
from datetime import date
from Domain.Car import Car
import datetime
class TransactionService():
    '''
    Manages transaction logic
    '''
    def __init__(self,repo,carService):
        """
        Creates a transaction service.
        """
        self.__repo=repo
        self.carService= carService
    def add_transaction(self,id,idCar,idCard,sumaP,sumaM,date,hour):
        '''
        Creates and add a transaction in the list.
        :param id: -int
        :param idCar: -int
        :param idCard: -int
        :param sumaP: -float
        :param sumaM: -float
        :param date: -str
        :param hour: str
        :return:
        '''
        errors = []
        if id in self.__repo.getAll():
            errors.append('Exista deja o tranzactie cu id-ul []'.format(id))
        if errors != []:
            raise ValueError(errors)
        tran = Transaction(id,idCar,idCard,sumaP,sumaM,date,hour)
        # self.__repo.addCar(self,car)
        self.__repo.addTransaction(tran)
    def getAll(self):
        """
        :return: a list of all the transactions.
        """
        return self.__repo.getAll()

    def remove_transaction(self,id):

        '''   errors=[]
        if car not in self.__carsList:
            errors.append("Masina nu exista in lista!")
        if errors!=[]:
            raise ValueError(errors)
        '''
        self.__repo.removeTransaction(id)

    def update_transaction(self,id,newId,newIdCar,newIdCard,newSumaP,newSumaM,newDate,newHour):
        '''
        Modifica o tranzactie.
        :param id: -int
        :param newId: -int
        :param newIdCar: -int
        :param newIdCard:-int
        :param newSumaP:-float
        :param newSumaM:-float
        :param date: -str
        :param hour: -str
        :return:
        '''
        self.__repo.updateTransaction(id, newId,newIdCar,newIdCard,newSumaP,newSumaM,newDate,newHour)
    def reducere(self):
        '''
        Afiseaza suma manoperei si reducerea de 10% aplicata pentru tranzactiile care contin un card client.
        :return: {sumaM: reducerea de 10%} -dict
        '''
        dict={}
        tranList=self.__repo.getAll()
        for tran in tranList:
            if tran.getIdCard()!=0:
                reducere=(10/100)*(float(tran.getSumaM()))
                suma=float(tran.getSumaM())-reducere
                reducere=str(round(reducere,2))
                dict[tran.getSumaM()]=reducere
                tran.setSumaM(float(suma))
        return dict
    def guarantee(self):
        '''
        Afiseaza pretul si reducerea masinilor aflate in garantie sub forma unnui dictionar.
        Daca masina este in garantie atunci suma pieselor devine 0.
        :return: {sumaP :0}-dict
        '''
        dict={}
        carsList= self.carService.get_all()
        tranList=self.__repo.getAll()
        for car in carsList:
            for j in range(len(tranList)):
                tran=tranList[j]
                if car.getGuarantee()=="da":
                    if int(car.getCarId())==int(tran.getIdCar()):
                        dict[tran.getSumaP()]=0
                        tran.setSumaP(0)
        return dict
    def show_tranzactions(self,op,suma1,suma2):
        '''
        Afiseaza tranzactiile cu suma cuprinsa intr-un interval dat. ( suma pieselor/suma manoperei)
        :param op:-optiunea ( sumaP/sumaM)-str
        :param suma1:-float
        :param suma2:-float
        :return:-lista tranzactiilor cu suma cuprinsa in intervalul dat -list
        '''
        tranList=self.__repo.getAll()
        newlist=[]
        if op=="sumaP":
            for i in range(len(tranList)):
                tran=tranList[i]
                sumaP=tran.getSumaP()
                if sumaP>=suma1 and sumaP<=suma2:
                    newlist.append(str(tran))
        elif op=="sumaM":
            for i in range(len(tranList)):
                tran=tranList[i]
                sumaM=tran.getSumaM()
                if sumaM>=suma1 and sumaM<=suma2:
                    newlist.append(str(tran))
        string =str(newlist[:])
        comp = string.split(",")
        return comp

    def order_tran_desc_reducere(self):
        '''
        Ordoneaza tranzactiile descrescator in functie de reducerile obtinute.
        Creaza o lista in care pastreaza id-ul fiecarui card client caruia i s-a aplicat reducerea.
        :return:-lista cu id-urile cardurilor client -list
        '''
        self.reducere()
        lista=sorted(self.__repo.getAll(), key=lambda tran: tran.getSumaM(), reverse=True)
        lista1=[]
        for tran in lista:
            lista1.append(tran.getIdCard())

        return lista1
    def show_transaction_data(self,data1,data2):
        '''
        Sterge toate tranzactiile cuprinse intr-un interval de zile dat.
        :param data1: -str (dd.mm.yyyy)
        :param data2: -str (dd.mm.yyyy)
        :return: -lista cu tranzactiile ramse-list
        '''
        newList=[]
        tranList=self.__repo.getAll()
        string1 = str(data1)
        comp1 = string1.split(".")
        day1= int(comp1[0])
        month1 = int(comp1[1])
        year1 = int(comp1[2])
        d1= date(year1,month1,day1)
        string2 = str(data2)
        comp2 = string2.split(".")
        day2 = int(comp2[0])
        month2 = int(comp2[1])
        year2 = int(comp2[2])
        d2=date(year2,month2,day2)
        for tran in tranList:
            string = str(tran.getDate())
            comp = string.split(".")
            day=int(comp[0])
            month=int(comp[1])
            year=int(comp[2])
            d=date(year,month,day)
            if d1<d<d2:
                self.__repo.removeTransaction(tran.getTId())
                newList.append(str(tran))
        return newList




























