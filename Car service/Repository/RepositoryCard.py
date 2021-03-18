import datetime
from Domain.Card import Card
fileName="carduri.txt"
class RepositoryCard():
    def __init__(self,fileName):
        self.__fileName=fileName
        self.__cardsList=[]
        self.__readFile()

    def addCard(self,card):
        self.__cardsList.append(card)
        self.__writeToFile()
    def removeCard(self,cardId):
        for i in range(len(self.__cardsList)):
            card=[]
            card=self.__cardsList[i]
            if card.getCardId()==cardId:
                card.setCarDel("True")
            else:
                card.setCarDel("False")
        car = self.getAll()


    def updateCard(self, id, newId, newName, newFirstName, newCNP, newDateB,newDateR):
        for card in self.__cardsList:
            idl=int(card.getCardId())
            if idl==int(id):
                if newId == "":
                    card.setId(id)
                else:
                    card.setId(newId)
                if newName== "":
                    card.setName(card.getName())
                else:
                    card.setName(newName)
                if  newFirstName== "":
                    card.setFirstName(str(card.getFirstName()))
                else:
                    card.setFirstName(newFirstName)
                if newCNP == "":
                    card.setCNP(card.getCNP())
                else:
                    card.setCNP(newCNP)
                if newDateB== "":
                    card.setDateB(card.getDateB())
                else:
                    card.setDateB(newDateB)
                if newDateR=="":
                    card.setDateR(card.getDateR())
                else:
                    card.setDateR(newDateR)
        self.__writeToFile()


    def getAll(self):
        return self.__cardsList[:]

    def eraseFile(self):
        f = open(self.__fileName, 'w').close()

    def __writeToFile(self):
        '''
        Scrie un card  intr-un  fisier.
        :return:
        '''
        content=""
        for card in self.__cardsList:
            cardString="/".join([str(card.getCardId()),card.getName(),card.getFirstName(),str(card.getCNP()),card.getDateB(),card.getDateR()])
            content=content+cardString+"\n"
        f=open(self.__fileName,'w')
        f.write(content)
        f.close()
    def __readFile(self):
        '''
        Citeste o lista de carduri dintr-un fisier.
        :return: lista de carduri
        '''
        f=open(self.__fileName,'r')
        try:
            lines=f.readlines()
            for line in lines:
                str=line[:-1]
                comp=str.split("/")
                id=int(comp[0])
                name=comp[1]
                firstName=comp[2]
                CNP=int(comp[3])
                dateB=comp[4]
                dateR=comp[5]
                c=Card(id,name,firstName,CNP,dateB,dateR)
                self.__cardsList.append(c)
        except Exception as e:
            print("fisierul este gol")
        f.close()


