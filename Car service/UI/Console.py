from tests.domainTests import test_transaction1,test_car1,test_car2,test_card1,test_card2,test_transaction2
from tests.serviceTests import add_car_test, remove_car_test,update_car_test,add_card_test,remove_card_test,update_card_test,add_transaction_test,remove_transaction_test,update_transaction_test,test_search_car,test_update_car_garantie,test_order_car_desc,test_search_client,test_reducere,test_guarantee,test_show_transactions,test_show_transactions_data
fileName="masini.txt"
class Console:

    def __init__(self, carService,cardService,transactionService):
        #self.__car_service=car_service
        self.carService = carService
        self.cardService = cardService
        self.transactionService= transactionService


    def show_menu(self):
        print('1. Masini')
        print('2. Carduri')
        print('3. Tranzactii')
        print('x. Exit')

    def run_console(self):
        # test_show_transactions_data()
        # test_show_transactions()
        # test_guarantee()
        # test_reducere()
        # test_search_client()
        # test_update_car_garantie()
        # test_search_car()
        # update_transaction_test()
        # remove_transaction_test()
        # add_transaction_test()
        # update_card_test()
        # remove_card_test()
        # add_card_test()
        # update_car_test()
        # remove_car_test()
        # add_car_test()
        # test_car1()
        # test_car2()
        # test_card1()
        # test_card2()
        # test_transaction2()
        # test_transaction1()

        while True:
            #try:
            self.show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.show_masini()
            elif op=='2':
                self.show_carduri()
            elif op=='3':
                self.show_tranzactii()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')
            #except Exception as e:
            #    print("Error: "+ str(e))


    def show_masini(self):

        while True:
            self.show_menu_masini()
            op = input('Optiune: ')
            if op == '1':
                self.handle_masini_add()
                print(self.handle_masini_show())
            elif op=='2':
                idCar=int(input("Dati id-ul masinii pe care doriti sa o stergeti: "))
                self.handle_masini_remove(idCar)
                print(self.handle_masini_show())
            elif op=='3':
                id=input("Dati id-ul masinii pe  care doriti sa o modificati: ")
                newid=input("Dati noul id: ")
                newModel=input("Dati noul model: ")
                newYear=input("Dati noul an de fabricatie: ")
                newNoKm=input("Dati numarul de km: ")
                newGuarantee=input("In garantie?: ")
                self.handle_masini_update(id,newid,newModel,newYear,newNoKm,newGuarantee)
                print(self.handle_masini_show())
            elif op=='4':
                caract=input("Dati caracteristica dupa care vreti sa cautati masina (model, an fabricatie, nr.Km, garantie) : ")
                if caract=='model':
                    word=str(input("Dati modelul masinii: "))
                elif caract=="an fabricatie":
                    word=int(input("Dati anul fabricatiei: "))
                elif caract=="nr.km":
                    word=int(input("Dati numarul de km: "))
                elif caract=="garantie":
                    word=str(input("In garantie?" ))
                print("LISTA COMPLETA BDE MASINI ESTE: ")
                print(self.handle_masini_show())
                print("\n")
                print("LISTA CU MASINILE CAUTATE ESTE: ")
                print("--------------------------------------------------------------------------------------------------------------------")

                self.handle_masini_search(caract,word)
            elif op=='5':

                self.handle_tranzactii_show()
                print("--------------------------------------------------------------------------------------------------------------------")
                self.handle_order_car_desc()
            elif op=='6':
                self.handle_cars_garantie()
                print(self.handle_masini_show())


            elif op=='a':
                self.handle_masini_show()

            elif op == 'b':
                break
            else:
                print('Comanda invalida!')
    def show_carduri(self):

        while True:
            self.show_menu_carduri()
            op = input('Optiune: ')
            if op == '1':
                self.handle_carduri_add()
                print(self.handle_carduri_show())
            elif op=='2':
                idCard=int(input("Dati id-ul cardului pe care doriti sa il stergeti: "))
                self.handle_carduri_remove(idCard)
                print(self.handle_carduri_show())
            elif op=='3':
                id=input("Dati id-ul cardului pe  care doriti sa il modificati: ")
                newid=input("Dati noul id: ")
                newName=input("Dati numele: ")
                newFirstName=input("Dati prenumele: ")
                newCNP=input("Dati CNP-ul: ")
                newDateB=input("Dati data nasterii: ")
                newDateR=input("Dati data inregistrarii: ")
                self.handle_carduri_update(id,newid,newName,newFirstName,newCNP,newDateB,newDateR)
                print(self.handle_carduri_show())
            elif op=='4':
                caract=input("Dati caracteristica dupa care vreti sa cautati clientul (nume, prenume, data nasterii, data inregistrarii) : ")
                if caract=='nume':
                    word=str(input("Dati numele clientului: "))
                    word2=str(input("Dati prenumele clientului: "))
                elif caract=='prenume':
                    word=str(input("Dati prenumele clientului: "))
                    word2=str(input("Dati numele clientului: "))
                elif caract=="CNP":
                    word=int(input("Dati CNP-ul clientului: "))
                elif caract=="data nasterii":
                    word=str(input("Dati data nasterii: "))
                elif caract=="data inregistrarii":
                    word=str(input("Dati data inregistrarii:" ))
                print(self.handle_carduri_show())
                self.handle_clienti_search(caract,word,word2)
            elif op=='5':
                print("LISTA MASINI: ")

                self.handle_masini_show()

                print("LISTA TRANZACTII:")

                print("--------------------------------------------------------------------------------------------------------------------")

                self.handle_tranzactii_show()
                self.transactionService.reducere()
                print("LISTA TRANZACTII DUPA REDUCERE: ")

                print("--------------------------------------------------------------------------------------------------------------------")

                self.handle_tranzactii_show()
                print("LISTA MASINI IN ORDINEA DESCRESCATOARE A REDUCERILOR: ")

                print("--------------------------------------------------------------------------------------------------------------------")
                lista=self.transactionService.order_tran_desc_reducere()
                self.handle_card_order_desc(lista)

            elif op=='a':
                self.handle_carduri_show()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def show_tranzactii(self):
        while True:
            self.show_menu_tranzactii()
            op = input('Optiune: ')
            if op == '1':
                self.handle_tranzactii_add()
                print(self.handle_tranzactii_show())
            elif op=='2':
                id=int(input("Dati id-ul tranzactiei pe care doriti sa o stergeti: "))
                self.handle_tranzactii_remove(id)
                print(self.handle_tranzactii_show())
            elif op=='3':
                id=input("Dati id-ul tranzactiei pe  care doriti sa o modificati: ")
                newid=input("Dati noul id: ")
                newIdCar=input("Dati id-ul masinii: ")
                newIdCard=input("Dati ig-ul cardului: ")
                newSumaP=input("Dati suma pieselor: ")
                newSumaM=input("Dati  suma manoperei: ")
                newDate=input("Dati data: ")
                newHour=input("Dati ora: ")
                self.handle_tranzactii_update(id,newid,newIdCar,newIdCard,newSumaP,newSumaM,newDate,newHour)
                print(self.handle_tranzactii_show())
            elif op=='4':
                print(self.handle_tranzactii_show())
                print("--------------------------------------------------------------------------------------------------------------------")
                print("S-AU FACUT URMATOARELE REDUCERI: ")
                self.handle_tranzactii_reducere()
                print(" ")
                print(self.handle_tranzactii_show())
            elif op=='5':
                print(self.handle_masini_show())
                print("--------------------------------------------------------------------------------------------------------------------")
                self.handle_tranzactii_guarantee()
                print("--------------------------------------------------------------------------------------------------------------------")
                print(self.handle_tranzactii_show())
            elif op=='6':
                op=str(input('In functie de ce suma doriti sa afisam tranzactiile ( sumaP, sumaM)? : '))
                print("Dati intervalul: ")
                suma1=float(input("suma1: "))
                suma2=float(input("suma2: "))
                print(self.handle_tranzactii_show())
                print("--------------------------------------------------------------------------------------------------------------------")
                self.handle_show_tranzactions(op,suma1,suma2)
            elif op=='7':
                print("Dati intervalul de zile: ")
                data1=str(input(" Data1 (dd.mm.yyyy) : "))
                data2=str(input(" data2 (dd.mm.yyyy): "))
                print(self.handle_tranzactii_show())
                print("\n")
                print("TRANZACTIILE CARE SE INCADREAZA IN INTERVAL SUNT: ")

                print("--------------------------------------------------------------------------------------------------------------------")

                self.handle_transactions_data(data1,data2)

                print(self.handle_tranzactii_show())


            elif op=='a':
                self.handle_tranzactii_show()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def show_menu_masini(self):
        print('--- MASINI')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Cautare masina.')
        print('5.Ordoneaza masinile descrescator dupa suma obtinuta pe manopera.')
        print('6.Actalizeaza garantiile masinilor (3+ ani, 60000+ km.')
        print('a. Afisare')
        print('b. Back')
    def show_menu_carduri(self):
        print('--- CARDURI')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Cautare card client')
        print('5.Ordoneaza cardurile client descrescator dupa reducerile acordate.')
        print('a. Afisare')
        print('b. Back')

    def show_menu_tranzactii(self):
        print('--- TRANZACTII')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Aplicati reducerea pretului namoperei pentru fiecare client care detine card.')
        print('5.Afisati pretul si reducerea pieselor masinilor care sunt in garantie: ')
        print('6.Afisati toate tranzactiile a caror suma este cuprinsa intr-un interval dat.')
        print('7.Afisati tranzactiile dintr-un interval de zile dat.')
        print('a. Afisare')
        print('b. Back')
    def handle_masini_add(self):
        try:
            id_car = int(input('ID: '))
            model=str(input("Model: "))
            year=int(input("Anul fabricatiei: "))
            noKm=int(input("Nr.km: "))
            guarantee=str(input("In garantie: "))
            self.carService.add_car(
                id_car,
                model,
                year,
                noKm,
                guarantee,
)
            print('Masina a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)
    def handle_carduri_add(self):
        try:
            id_card = int(input('ID: '))
            name=str(input("Name: "))
            firstName=str(input("First Name: "))
            CNP=int(input("CNP: "))
            dateB=str(input("Date of birth: "))
            dateR=str(input("Date of registration: "))
            self.cardService.add_card(
                id_card,
                name,
                firstName,
                CNP,
                dateB,
                dateR
            )
            print('Cardul clientului a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def handle_tranzactii_add(self):
        try:
            id = int(input('ID: '))
            idCar = int(input("Id Car: "))
            idCard = int(input("Id Card: "))
            sumaP= float(input("Suma piese: "))
            sumaM = float(input("Suma manopera: "))
            date= str(input("Date: "))
            hour=float(input("Hour: "))
            self.transactionService.add_transaction(
                id,
                idCar,
                idCard,
                sumaP,
                sumaM,
                date,
                hour)
            print(' Tranzactia a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def handle_masini_show(self):
        for car in self.carService.get_all():
            print(car)
    def handle_masini_remove(self,idCar):
        self.carService.remove_car(idCar)
    def handle_masini_remove1(self,idCar):
        self.carService.remove_car1(idCar)
    def handle_masini_update(self,id,newId,newModel,newYear,newNoKm,newGuarantee):
        self.carService.update_car(id,newId,newModel,newYear,newNoKm,newGuarantee)
    def handle_masini_search(self,caract,word):
        comp=self.carService.search_car(caract,word)
        for i in range(len(comp)):
            if i == len(comp)-1:
                print(comp[i])
            else:
                print(comp[i], end="\n")
    def handle_order_car_desc(self):
        comp=self.carService.order_car_desc()
        for i in range(len(comp)):
            if i == len(comp)-1:
                print(comp[i])
            else:
                print(comp[i], end="\n")
    def handle_cars_garantie(self):
        self.carService.update_cars_garantie()
    def handle_carduri_show(self):
        for card in self.cardService.getAll():
            print(card)
    def handle_carduri_remove(self,idCard):
        self.cardService.remove_card(idCard)
    def handle_carduri_update(self,id,newId,newName,newFirstName,newCNP,newDateB,newDateR):
        self.cardService.update_card(id,newId,newName,newFirstName,newCNP,newDateB,newDateR)
    def handle_card_order_desc(self,lista):
        comp=self.cardService.order_card_desc(lista)
        for i in range(len(comp)):
            if i == len(comp)-1:
                print(comp[i])
            else:
                print(comp[i], end="\n")
    def handle_clienti_search(self,caract,word,word2):
        print(self.cardService.search_client(caract,word,word2))
    def handle_tranzactii_show(self):
        for tran in self.transactionService.getAll():
            print(tran)
    def handle_tranzactii_remove(self,id):
        self.transactionService.remove_transaction(id)
    def handle_tranzactii_update(self, id, newId,newIdcar,newIdCard,newSumaP,newSumaM,newdate,newHour):
        self.transactionService.update_transaction(id, newId,newIdcar,newIdCard,newSumaP,newSumaM,newdate,newHour)
    def handle_tranzactii_reducere(self):
        print(self.transactionService.reducere())
    def handle_tranzactii_guarantee(self):
        print(self.transactionService.guarantee())
    def handle_show_tranzactions(self,op,suma1,suma2):
        comp= self.transactionService.show_tranzactions(op,suma1,suma2)
        for i in range(len(comp)):
            if i == len(comp)-1:
                print(comp[i])
            else:
                print(comp[i], end="\n")
    def handle_transactions_data(self,data1,data2):
        comp=self.transactionService.show_transaction_data(data1,data2)
        for i in range(len(comp)):
            if i == len(comp)-1:
                print(comp[i])
            else:
                print(comp[i], end="\n")















