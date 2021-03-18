from Domain.Car import Car
from Domain.Card import Card
from Domain.Transaction import Transaction
def test_car1():
    car=Car(1,"Mercedes",2008,123000,"da")
    assert car.getCarId()==1
    assert car.getModel()=="Mercedes"
    assert car.getYear()==2008
    assert car.getNoKm()==123000
    assert car.getGuarantee()=="da"
test_car1()
def test_car2():
    car = Car(1, "Mercedes", 2008, 123000, "da")
    car.setId(2)
    assert car.getCarId()==2
    car.setModel("BMW")
    assert car.getModel()=="BMW"
    car.setYear(2003)
    assert car.getYear()==2003
    car.setNoKm(100000)
    assert car.getNoKm()==100000
    car.setGuarantee("nu")
    assert car.getGuarantee()=="nu"
test_car2()
def test_card1():
    card=Card(1,"Monica","Tanasa",6000923271718,"23.09.2000","07.12.2018")
    assert  card.getCardId()==1
    assert card.getName()=="Monica"
    assert card.getFirstName()=="Tanasa"
    assert card.getCNP()==6000923271718
    assert card.getDateB()=="23.09.2000"
    assert card.getDateR()=="07.12.2018"
test_card1()
def test_card2():
    card = Card(1, "Monica", "Tanasa", 6000923271718, "23.09.2000", "07.12.2018")
    card.setId(2)
    assert card.getCardId()==2
    card.setCNP(6000923271719)
    assert card.getCNP()==6000923271719
    card.setName("Andra")
    assert card.getName()=="Andra"
    card.setFirstName("Trifan")
    assert card.getFirstName()=="Trifan"
    card.setDateB("24.09.2000")
    assert card.getDateB()=="24.09.2000"
    card.setDateR("08.12.2018")
    assert card.getDateR()=="08.12.2018"
test_card2()
def test_transaction1():
    tran=Transaction(1,1,1,1200,700,"12.12.2009",13.30)
    assert tran.getTId()==1
    assert tran.getIdCar()==1
    assert tran.getIdCard()==1
    assert tran.getSumaP()==1200
    assert tran.getSumaM()==700
    assert tran.getDate()=="12.12.2009"
    assert tran.getHour()==13.30
test_transaction1()
def test_transaction2():
    tran = Transaction(1, 1, 1, 1200, 700, "12.12.2009", 13.30)
    tran.setTId(2)
    assert tran.getTId()==2
    tran.setIdCar(2)
    assert tran.getIdCar()==2
    tran.setIdCard(2)
    assert tran.getIdCard()==2
    tran.setSumaP(1300)
    assert tran.getSumaP()==1300
    tran.setSumaM(800)
    assert tran.getSumaM()==800
    tran.setDate("13.12.2009")
    assert tran.getDate()=="13.12.2009"
    tran.setHour(13.00)
    assert tran.getHour()==13.00




