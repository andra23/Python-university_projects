from Domain.Transaction import Transaction
fileName="tranzactii.txt"
class RepositoryTransaction():
    def __init__(self,fileName):
        self.__fileName=fileName
        self.__tranList=[]
        self.__readFile()

    def addTransaction(self,tran):
        self.__tranList.append(tran)
        self.__writeToFile()
    def removeTransaction(self,tranId):
        for i in range(len(self.__tranList)):
            tran=[]
            tran=self.__tranList[i]
            if tran.getTId()==tranId:
                tran.setCarDel("True")
            else:
                tran.setCarDel("False")
        car = self.getAll()


    def updateTransaction(self,id,newId,newIdCar,newIdCard,newSumaP,newSumaM,newDate,newHour):
        for tran in self.__tranList:
            idl=tran.getTId()
            if idl==int(id):
                if newId == "":
                    tran.setTId(id)
                else:
                    tran.setTId(newId)
                if newIdCar== "":
                    tran.setIdCar(tran.getIdCar())
                else:
                    tran.setIdCar(newIdCar)
                if  newIdCard== "":
                    tran.setIdCard(tran.getIdCard())
                else:
                    tran.setIdCard(newIdCard)
                if newSumaP == "":
                    tran.setSumaP(tran.getSumaP())
                else:
                    tran.setSumaP(newSumaP)
                if newSumaM== "":
                    tran.setSumaM(tran.getSumaP())
                else:
                    tran.setSumaM(newSumaM)
                if newDate=="":
                    tran.setDate(tran.getDate())
                else:
                    tran.setDate(newDate)
                if newHour=="":
                    tran.setHour(tran.getHour())
                else:
                    tran.setHour(newHour)
        self.__writeToFile()


    def getAll(self):
        return self.__tranList[:]

    def eraseFile(self):
        f = open(self.__fileName, 'w').close()

    def __writeToFile(self):
        '''
        Scrie o tranzactie intr-un fisier.
        :return:
        '''
        content = ""
        for tran in self.__tranList:
            tranString = "/".join([str(tran.getTId()),str(tran.getIdCar()), str(tran.getIdCard()), str(tran.getSumaP()), str(tran.getSumaM()),tran.getDate(),str(tran.getHour())])
            content = content + tranString + "\n"
        f = open(self.__fileName, 'w')
        f.write(content)
        f.close()

    def __readFile(self):
        '''
        Citeste o lista de tranzactii dintr-un fisier.
        :return: lista de tranzactii
        '''
        f = open(self.__fileName, 'r')
        try:
            lines = f.readlines()
            for line in lines:
                str = line[:-1]
                comp = str.split("/")
                id = int(comp[0])
                idCar= int(comp[1])
                idCard= int(comp[2])
                sumaP= float(comp[3])
                sumaM= float(comp[4])
                date=comp[5]
                hour=float(comp[6])
                c = Transaction(id,idCar,idCard,sumaP,sumaM,date,hour)
                self.__tranList.append(c)
        except Exception as e:
            print("fisierul este gol")

        f.close()






