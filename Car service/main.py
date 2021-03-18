from Repository.RepositoryCar import RepositoryCar
from Repository.RepositoryCard import RepositoryCard
from Repository.RepositoryTransaction import RepositoryTransaction
from Service.CarService import CarService
from Service.CardService import CardService
from Service.TransactionService import TransactionService
from UI.Console import Console
if __name__ == '__main__':
    repoCar = RepositoryCar("masini.txt")
    repoCard= RepositoryCard("carduri.txt")
    repoTran= RepositoryTransaction("tranzactii.txt")
    serviceCar = CarService(repoCar,repoTran)
    serviceCard=CardService(repoCard)
    serviceTransaction = TransactionService(repoTran,serviceCar)
    console = Console(serviceCar,serviceCard,serviceTransaction)
    console.run_console()