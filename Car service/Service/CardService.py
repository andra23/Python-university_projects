from Domain.Card import Card

from Service.TransactionService import TransactionService
import datetime
class CardService():
    '''
    Manages card logic
    '''
    def __init__(self,repo):
        """
        Creates a card service.
        """

        self.__repo=repo

    def add_card(self,idCard,name,fisrtName,CNP,dateB,dateR):
        '''
        Creates and add a card in the cards list.
        :param idCard: -int
        :param name: -str
        :param fisrtName: -str
        :param CNP: -int,unic
        :param dateB: -str
        :param dateR: -str
        :return:
        '''
        errors = []
        if idCard in self.__repo.getAll():
            errors.append('Exista deja un card cu id-ul []'.format(idCard))
        if CNP in self.__repo.getAll():
            errors.append("CNP-ul trebuie sa fie unic! Exista deja o persoana inregistrata cu acest CNP.")
        if len(str(CNP))<13 or len(str(CNP))>13:
            errors.append("CNP-ul trebuie sa aiba exact 13 cifre!")
        if errors != []:
           raise ValueError(errors)
        card = Card(idCard,name,fisrtName,CNP,dateB,dateR)
       #self.__repo.addCar(self,car)
        self.__repo.addCard(card)
    def getAll(self):
        """
        :return: a list of all the cars.
        """
        return self.__repo.getAll()
    def remove_card(self,cardId):

        '''   errors=[]
        if car not in self.__carsList:
            errors.append("Masina nu exista in lista!")
        if errors!=[]:
            raise ValueError(errors)
        '''
        self.__repo.removeCard(cardId)

    def update_card(self,id,newId,newName,newFirstName,newCNP,newDateB,newDateR):
        '''
        Modifica un card care se identifica dupa id.
        :param idCard: -int
        :param name: -str
        :param fistName: -str
        :param CNP: int,unic
        :param dateB: -str
        :param dateR: -str
        :return:
        '''
        self.__repo.updateCard(id,newId,newName,newFirstName,newCNP,newDateB,newDateR)

    def search_client(self, caract, word,word2):
        '''
        Cauta clientii in functie de anumite caracteristici (nume,prenume,CNP,data nasterii.data inregistrarii.
        :param caract: categoria dupa care se face cautarea
        :param word: -caracteristica clienutlui -str
        :param word2: -in cazul in care se doreste cautare dupa nume/prenume , daca exista doua nume identice se cere si prenumele -str
        :return:
        '''
        newList = []
        cardsList = self.__repo.getAll()
        for i in range(len(cardsList)):
            card = cardsList[i]
            if caract == "nume":
                if card.getName() == word:
                    if card.getFirstName()==word2:
                        newList.append(str(cardsList[i]))
            elif caract=="prenume":
                if card.getFirstName()==word:
                    if card.getName()==word2:
                        newList.append(str(cardsList[i]))
            elif caract == "CNP":
                if card.getCNP() == word:
                    newList.append(str(cardsList[i]))
            elif caract == "data nasterii":
                if card.getDateB() == word:
                    newList.append(str(cardsList[i]))
            elif caract == "data inregistrarii":
                if card.getGuarantee() == word:
                    newList.append(str(cardsList[i]))
        return newList
    def order_card_desc(self,lista):
        '''
        Ordoneaza cardurile cliend descrescator dupa valoarea reducerilor obtinute.
        :param lista:-lista cu id-ul fiecarui card ordonata in functiile de reducerile aplicate pe suma manoperei
        :return:-lista ordonata cu carduri client
        '''
        cardsList=self.__repo.getAll()
        newList=[]
        for i in range(len(lista)):
            for j in range(len(cardsList)):
                card=cardsList[j]
                if lista[i]==int(card.getCardId()):
                    newList.append(str(card))
        string=str(newList[:])
        comp = string.split(",")
        return comp














