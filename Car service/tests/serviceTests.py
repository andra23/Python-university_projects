from Service.CardService import CardService
from Repository.RepositoryCar import RepositoryCar
from Repository.RepositoryCard import RepositoryCard
from Repository.RepositoryTransaction import RepositoryTransaction
from Domain.Car import Car
from Domain.Card import Card
from Domain.Transaction import Transaction
from Service.CarService import CarService
from Service.TransactionService import TransactionService
def add_car_test():
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    assert len(repoCar.getAll()) ==0
    car = Car(1,"Mercedes",2019,0,"da")
    car_service.add_car(car.getCarId(),
                        car.getModel(),
                        car.getYear(),
                        car.getNoKm(),
                        car.getGuarantee())
    assert len(repoCar.getAll()) ==1
    repoCar.eraseFile()

def remove_car_test():
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    repoCar.eraseFile()
    car= Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car.getCarId(),
                        car.getModel(),
                        car.getYear(),
                        car.getNoKm(),
                        car.getGuarantee())
    assert len(repoCar.getAll()) == 1
    car2=Car(2,"Audi",2008,130000,"da")
    car_service.add_car(car2.getCarId(),
                        car2.getModel(),
                        car2.getYear(),
                        car2.getNoKm(),
                        car2.getGuarantee())
    assert len(repoCar.getAll())==2
    car_service.remove_car(car.getCarId())
    assert len(repoCar.getAll())==1
    repoCar.eraseFile()

def update_car_test():
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    repoCar.eraseFile()
    car = Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car.getCarId(),
                        car.getModel(),
                        car.getYear(),
                        car.getNoKm(),
                        car.getGuarantee())
    assert car.getModel()=="Mercedes"
    car_service.update_car(1,"","bmw","","","")
    car1= repoCar.getAll()[0]
    assert car1.getModel()=="bmw"
    repoCar.eraseFile()

def add_card_test():
    repoCard = RepositoryCard("carduriTests.txt")
    card_service = CardService(repoCard)
    assert len(repoCard.getAll()) == 0
    card = Card(1,"Tanasa","Monica",6000923271718,"23.09.2000","12.12.2018")
    card_service.add_card(card.getCardId(),
                        card.getName(),
                        card.getFirstName(),
                        card.getCNP(),
                        card.getDateB(),
                        card.getDateR())
    assert len(repoCard.getAll()) == 1
    repoCard.eraseFile()
def remove_card_test():
    repoCard = RepositoryCard("carduriTests.txt")
    card_service = CardService(repoCard)
    repoCard.eraseFile()
    card = Card(1, "Tanasa", "Monica", 6000923271718, "23.09.2000", "12.12.2018")
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR())
    assert len(repoCard.getAll()) == 1
    card2= Card(2, "Tanasa", "Sorina", 6000923271719, "23.06.2000", "13.12.2018")
    card_service.add_card(card2.getCardId(),
                          card2.getName(),
                          card2.getFirstName(),
                          card2.getCNP(),
                          card2.getDateB(),
                          card2.getDateR())
    assert len(repoCard.getAll()) == 2
    card_service.remove_card(card.getCardId())
    assert len(repoCard.getAll()) == 1
    repoCard.eraseFile()
def update_card_test():
    repoCard = RepositoryCard("carduriTests.txt")
    card_service = CardService(repoCard)
    card = Card(1, "Tanasa", "Monica", 6000923271718, "23.09.2000", "12.12.2018")
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR())
    card_service.update_card(1,"","","Andreea","","","")
    card2=repoCard.getAll()[0]
    assert card2.getFirstName()=="Andreea"
    repoCard.eraseFile()
def add_transaction_test():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    tran_service = TransactionService(repoTran,car_service)
    assert len(repoTran.getAll()) == 0
    tran = Transaction(1,1,1,1200,700,"12.12.2010",13.30)
    tran_service.add_transaction(tran.getTId(),
                          tran.getIdCar(),
                          tran.getIdCard(),
                          tran.getSumaP(),
                          tran.getSumaM(),
                          tran.getDate(),
                          tran.getHour())
    assert len(repoTran.getAll()) == 1
    repoTran.eraseFile()
def remove_transaction_test():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    tran_service = TransactionService(repoTran, car_service)
    repoTran.eraseFile()
    assert len(repoTran.getAll()) == 0
    tran = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran.getTId(),
                                 tran.getIdCar(),
                                 tran.getIdCard(),
                                 tran.getSumaP(),
                                 tran.getSumaM(),
                                 tran.getDate(),
                                 tran.getHour())
    assert len(repoTran.getAll()) == 1
    tran2 = Transaction(2, 2, 2, 1700.50, 800, "09.12.2010", 14.00)
    tran_service.add_transaction(tran.getTId(),
                                 tran.getIdCar(),
                                 tran.getIdCard(),
                                 tran.getSumaP(),
                                 tran.getSumaM(),
                                 tran.getDate(),
                                 tran.getHour())

    assert len(repoTran.getAll()) == 2
    tran_service.remove_transaction(tran.getTId())
    assert len(repoTran.getAll()) == 1
    repoTran.eraseFile()
def update_transaction_test():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar,"")
    repoTran.eraseFile()
    tran_service = TransactionService(repoTran, car_service)
    tran = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran.getTId(),
                                 tran.getIdCar(),
                                 tran.getIdCard(),
                                 tran.getSumaP(),
                                 tran.getSumaM(),
                                 tran.getDate(),
                                 tran.getHour())
    assert len(repoTran.getAll()) == 1
    tran_service.update_transaction(1,"","","",1300,"","","")
    tran1=repoTran.getAll()[0]
    assert tran1.getSumaP()==1300
    repoTran.eraseFile()

def test_search_car():
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    repoCar.eraseFile()
    car1 = Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car1.getCarId(),
                        car1.getModel(),
                        car1.getYear(),
                        car1.getNoKm(),
                        car1.getGuarantee())
    car2 = Car(2, "Ford", 2008, 120000, "nu")
    car_service.add_car(car2.getCarId(),
                        car2.getModel(),
                        car2.getYear(),
                        car2.getNoKm(),
                        car2.getGuarantee())
    car3=Car(3,"bmw",2018,100000,"nu")
    car_service.add_car(car3.getCarId(),
                        car3.getModel(),
                        car3.getYear(),
                        car3.getNoKm(),
                        car3.getGuarantee())
    assert len(repoCar.getAll())==3
    l=car_service.search_car("model","Ford")
    assert l[0]==str(car2)
    repoCar.eraseFile()
def test_update_car_garantie():
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    repoCar.eraseFile()
    car1 = Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car1.getCarId(),
                        car1.getModel(),
                        car1.getYear(),
                        car1.getNoKm(),
                        car1.getGuarantee())
    car2 = Car(2, "Ford", 2007, 120000, "da")
    car_service.add_car(car2.getCarId(),
                        car2.getModel(),
                        car2.getYear(),
                        car2.getNoKm(),
                        car2.getGuarantee())
    car3 = Car(3, "bmw", 2001, 100000, "nu")
    car_service.add_car(car3.getCarId(),
                        car3.getModel(),
                        car3.getYear(),
                        car3.getNoKm(),
                        car3.getGuarantee())
    assert len(repoCar.getAll()) == 3
    car_service.update_cars_garantie()
    car=repoCar.getAll()[1]
    assert car1.getGuarantee()=="da"
    assert car.getGuarantee()=="nu"
    assert car3.getGuarantee()=="nu"
    repoCar.eraseFile()

def test_order_car_desc():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    tran_service = TransactionService(repoTran, car_service)
    tran1 = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran1.getTId(),
                                 tran1.getIdCar(),
                                 tran1.getIdCard(),
                                 tran1.getSumaP(),
                                 tran1.getSumaM(),
                                 tran1.getDate(),
                                 tran1.getHour())
    tran2 = Transaction(2, 2, 2, 2000, 1300, "12.12.2010", 13.30)
    tran_service.add_transaction(tran2.getTId(),
                                 tran2.getIdCar(),
                                 tran2.getIdCard(),
                                 tran2.getSumaP(),
                                 tran2.getSumaM(),
                                 tran2.getDate(),
                                 tran2.getHour())
    tran3 = Transaction(3, 3, 3, 800, 450, "12.12.2010", 13.30)
    tran_service.add_transaction(tran3.getTId(),
                                 tran3.getIdCar(),
                                 tran3.getIdCard(),
                                 tran3.getSumaP(),
                                 tran3.getSumaM(),
                                 tran3.getDate(),
                                 tran3.getHour())
    assert len(repoTran.getAll())==3
    car1 = Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car1.getCarId(),
                        car1.getModel(),
                        car1.getYear(),
                        car1.getNoKm(),
                        car1.getGuarantee())
    car2 = Car(2, "Ford", 2007, 120000, "da")
    car_service.add_car(car2.getCarId(),
                        car2.getModel(),
                        car2.getYear(),
                        car2.getNoKm(),
                        car2.getGuarantee())
    car3 = Car(3, "bmw", 2001, 100000, "nu")
    car_service.add_car(car3.getCarId(),
                        car3.getModel(),
                        car3.getYear(),
                        car3.getNoKm(),
                        car3.getGuarantee())
    assert len(repoCar.getAll()) == 3
    l=car_service.order_car_desc()
    l1=[car1,car2,car3]
    string = str(l1[:])
    comp = string.split(",")
    assert l==l1
    print(l)
    repoTran.eraseFile()
    repoCar.eraseFile()
def test_search_client():
    repoCard = RepositoryCard("carduriTests.txt")
    card_service = CardService(repoCard)
    repoCard.eraseFile()
    card = Card(1, "Tanasa", "Monica", 6000923271718, "23.09.2000", "12.12.2018")
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR())
    assert len(repoCard.getAll()) == 1
    card2 = Card(2, "Tanasa", "Sorina", 6000923271719, "23.06.2000", "13.12.2018")
    card_service.add_card(card2.getCardId(),
                          card2.getName(),
                          card2.getFirstName(),
                          card2.getCNP(),
                          card2.getDateB(),
                          card2.getDateR())
    assert len(repoCard.getAll()) == 2
    l=card_service.search_client("nume","Tanasa","Sorina")
    assert l[0]==str(card2)
    repoCard.eraseFile()
def test_reducere():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    tran_service = TransactionService(repoTran, car_service)
    tran1 = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran1.getTId(),
                                 tran1.getIdCar(),
                                 tran1.getIdCard(),
                                 tran1.getSumaP(),
                                 tran1.getSumaM(),
                                 tran1.getDate(),
                                 tran1.getHour())
    tran2 = Transaction(2, 2, 2, 2000, 1300, "12.12.2010", 13.30)
    tran_service.add_transaction(tran2.getTId(),
                                 tran2.getIdCar(),
                                 tran2.getIdCard(),
                                 tran2.getSumaP(),
                                 tran2.getSumaM(),
                                 tran2.getDate(),
                                 tran2.getHour())
    tran3 = Transaction(3, 3, 3, 800, 450, "12.12.2010", 13.30)
    tran_service.add_transaction(tran3.getTId(),
                                 tran3.getIdCar(),
                                 tran3.getIdCard(),
                                 tran3.getSumaP(),
                                 tran3.getSumaM(),
                                 tran3.getDate(),
                                 tran3.getHour())
    assert len(repoTran.getAll()) == 3
    dict1=tran_service.reducere()

    dict={}
    dict[700] = '70.0'
    dict[1300]='130.0'
    dict[450]='45.0'
    assert dict1==dict
    repoTran.eraseFile()
def test_guarantee():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    tran_service = TransactionService(repoTran, car_service)
    tran1 = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran1.getTId(),
                                 tran1.getIdCar(),
                                 tran1.getIdCard(),
                                 tran1.getSumaP(),
                                 tran1.getSumaM(),
                                 tran1.getDate(),
                                 tran1.getHour())
    tran2 = Transaction(2, 2, 2, 2000, 1300, "12.12.2010", 13.30)
    tran_service.add_transaction(tran2.getTId(),
                                 tran2.getIdCar(),
                                 tran2.getIdCard(),
                                 tran2.getSumaP(),
                                 tran2.getSumaM(),
                                 tran2.getDate(),
                                 tran2.getHour())
    tran3 = Transaction(3, 3, 3, 800, 450, "12.12.2010", 13.30)
    tran_service.add_transaction(tran3.getTId(),
                                 tran3.getIdCar(),
                                 tran3.getIdCard(),
                                 tran3.getSumaP(),
                                 tran3.getSumaM(),
                                 tran3.getDate(),
                                 tran3.getHour())
    assert len(repoTran.getAll()) == 3
    car1 = Car(1, "Mercedes", 2019, 0, "da")
    car_service.add_car(car1.getCarId(),
                        car1.getModel(),
                        car1.getYear(),
                        car1.getNoKm(),
                        car1.getGuarantee())
    car2 = Car(2, "Ford", 2008, 120000, "nu")
    car_service.add_car(car2.getCarId(),
                        car2.getModel(),
                        car2.getYear(),
                        car2.getNoKm(),
                        car2.getGuarantee())
    car3 = Car(3, "bmw", 2018, 100000, "nu")
    car_service.add_car(car3.getCarId(),
                        car3.getModel(),
                        car3.getYear(),
                        car3.getNoKm(),
                        car3.getGuarantee())
    assert len(repoCar.getAll()) == 3
    dict1=tran_service.guarantee()
    dict={}
    dict[1200]=0
    assert dict1==dict
    repoTran.eraseFile()
    repoCar.eraseFile()
def test_show_transactions():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    tran_service = TransactionService(repoTran, car_service)
    tran1 = Transaction(1, 1, 1, 1200, 700, "12.12.2010", 13.30)
    tran_service.add_transaction(tran1.getTId(),
                                 tran1.getIdCar(),
                                 tran1.getIdCard(),
                                 tran1.getSumaP(),
                                 tran1.getSumaM(),
                                 tran1.getDate(),
                                 tran1.getHour())
    tran2 = Transaction(2, 2, 2, 2000, 1300, "12.12.2010", 13.30)
    tran_service.add_transaction(tran2.getTId(),
                                 tran2.getIdCar(),
                                 tran2.getIdCard(),
                                 tran2.getSumaP(),
                                 tran2.getSumaM(),
                                 tran2.getDate(),
                                 tran2.getHour())
    tran3 = Transaction(3, 3, 3, 800, 450, "12.12.2010", 13.30)
    tran_service.add_transaction(tran3.getTId(),
                                 tran3.getIdCar(),
                                 tran3.getIdCard(),
                                 tran3.getSumaP(),
                                 tran3.getSumaM(),
                                 tran3.getDate(),
                                 tran3.getHour())
    assert len(repoTran.getAll()) == 3
    l=tran_service.show_tranzactions("sumaP",600,900)
    l1=[]
    l1.append(str(tran3))
    assert l[0]==str(l1)
    repoTran.eraseFile()
def test_show_transactions_data():
    repoTran = RepositoryTransaction("tranzactiiTests.txt")
    repoCar = RepositoryCar("masiniTests.txt")
    car_service = CarService(repoCar, "")
    tran_service = TransactionService(repoTran, car_service)
    tran1 = Transaction(1, 1, 1, 1200, 700, "09.03.2011", 13.30)
    tran_service.add_transaction(tran1.getTId(),
                                 tran1.getIdCar(),
                                 tran1.getIdCard(),
                                 tran1.getSumaP(),
                                 tran1.getSumaM(),
                                 tran1.getDate(),
                                 tran1.getHour())
    tran2 = Transaction(2, 2, 2, 2000, 1300, "12.12.2012", 13.30)
    tran_service.add_transaction(tran2.getTId(),
                                 tran2.getIdCar(),
                                 tran2.getIdCard(),
                                 tran2.getSumaP(),
                                 tran2.getSumaM(),
                                 tran2.getDate(),
                                 tran2.getHour())
    tran3 = Transaction(3, 3, 3, 800, 450, "12.12.2003", 13.30)
    tran_service.add_transaction(tran3.getTId(),
                                 tran3.getIdCar(),
                                 tran3.getIdCard(),
                                 tran3.getSumaP(),
                                 tran3.getSumaM(),
                                 tran3.getDate(),
                                 tran3.getHour())
    assert len(repoTran.getAll()) == 3
    l=tran_service.show_transaction_data("03.07.2010","12.12.2013")

    assert len(repoTran.getAll())==1
    repoTran.eraseFile()
































