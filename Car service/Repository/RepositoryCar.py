import os
from Domain.Car import Car
fileName="masini.txt"
class RepositoryCar():

    def __init__(self,fileName):
        self.__fileName=fileName
        self.__carsList=[]
        self.__readFile()

    def addCar(self,car):
        self.__carsList.append(car)
        self.writeToFile()

    def removeCar(self,carId):
        for i in range(len(self.__carsList)):
            car=self.__carsList[i]
            if int(car.getCarId())==carId:
                car.setCarDel("True")
            else:
                car.setCarDel("False")
        car=self.getAll()



    def eraseFile(self):
        f= open(self.__fileName, 'w').close()

    def updateCar(self, id, newId, newModel, newYear, newNoKm, newGuarantee):
        for car in self.__carsList:
            idl=int(car.getCarId())
            if idl==int(id):
                if newId == "":
                    car.setId(id)
                else:
                    car.setId(newId)
                if newModel== "":
                    car.setModel(car.getModel())
                else:
                    car.setModel(newModel)
                if  newYear== "":
                    car.setYear(car.getYear())
                else:
                    car.setYear(newYear)
                if newNoKm == "":
                    car.setNoKm(car.getNoKm())
                else:
                    car.setNoKm(newNoKm)
                if newGuarantee== "":
                    car.setGuarantee(car.getGuarantee())
                else:
                    car.setGuarantee(newGuarantee)
        self.writeToFile()

    def getAll(self):
        return self.__carsList[:]

    def writeToFile(self):
        '''
        Scrie o masina in fisier.
        :return:
        '''
        content=" "
        for car in self.__carsList:
            carString="/".join([str(car.getCarId()),car.getModel(),str(car.getYear()),str(car.getNoKm()),car.getGuarantee()])
            content=content+carString+"\n"
        f=open(self.__fileName,"w")
        f.write(content)
        f.close()

    def __readFile(self):
        '''
        Citeste o lista de masini dintr-un fisier.
        :return: lista de masini
        '''
        with open (self.__fileName, 'r') as f:
            try:
                for line in f:
                    str = line[:-1]
                    comp=str.split("/")
                    id=comp[0]
                    model=comp[1]
                    year=int(comp[2])
                    NoKm=float(comp[3])
                    #data=comp[3].split()
                    guarantee=comp[4]
                    c=Car(id,model,year,NoKm,guarantee)
                    self.__carsList.append(c)
            except Exception as e:
                print("fisierul este gol")
                f.close()




        # f=open(self.__fileName,'r')
        # #if os.path.getsize(self.__fileName)<=0:
        # #    raise Exception("empty file")
        # try:
        #     lines=f.readlines()
        #     for line in lines:
        #         str=line[:-1]
        #         comp=str.split("/")
        #         id=comp[0]
        #         model=comp[1]
        #         year=int(comp[2])
        #         NoKm=int(comp[3])
        #         #data=comp[3].split()
        #         guarantee=comp[4]
        #         c=Car(id,model,year,NoKm,guarantee)
        #         self.__carsList.append(c)
        # except Exception as e:
        #     print("fisierul este gol")
        # f.close()






