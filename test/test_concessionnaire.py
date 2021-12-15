from concessionnaire.vehicule import Vehicule, Voiture, Moto, Camion
from concessionnaire.magasin import Magasin
from concessionnaire.seller import Seller
from concessionnaire.client import Client
from concessionnaire.vente import Vente
import pytest
import os


@pytest.fixture
def vehicule_test():
    return Vehicule("Hiaris","Toyota","Rouge",10000, 20)

@pytest.fixture
def vehicule_test_in_store():
    return Moto("T500","Dukati","Verte",25000,30)

@pytest.fixture
def magasin_test():
    mon_magasin = Magasin("Rue Barthelemy Delespaul","084948384")
    mon_magasin.add_vehicle(Moto("T500","Dukati","Verte",25000,30))
    mon_magasin.add_vehicle(Camion("T500","Toyota","Verte",30000,30))
    mon_magasin.add_vehicle(Voiture("hybris","Toyota","Rouge",15000,30))
    mon_magasin.add_seller("Robert",False)
    return mon_magasin



class TestVehicule:
    def test_init(self,vehicule_test):
        assert vehicule_test.prix_TTC == 10000*1.2
        # test prix_HT init
        assert vehicule_test.prix_HT == 10000
        with pytest.raises(ValueError):
            Vehicule("Hiaris","Toyota","Rouge",10000.0, 20)
        # test reduction init
        assert vehicule_test.reduction == 20 
        with pytest.raises(ValueError):
            Vehicule("Hiaris","Toyota","Rouge",10000, 20.0)
        # test marque init   
        assert vehicule_test.marque == "Toyota"
        with pytest.raises(ValueError):
            Vehicule("Hiaris",20,"Rouge",10000, 20)
        assert vehicule_test.modele == "Hiaris"
        assert vehicule_test.couleur == "Rouge"

    def test_modify_HT(self,vehicule_test):
        vehicule_test.prix_HT = 2000
        assert vehicule_test.prix_TTC == 2000*1.2
    
    def test_prix_TTC_is_protected(self,vehicule_test):
        with pytest.raises(AttributeError):
            vehicule_test.prix_TTC = 300

    def test_final_price(self,vehicule_test):
        assert vehicule_test.final_price(True) == 9600
        assert vehicule_test.final_price(False) == vehicule_test.prix_TTC




class TestMagasin:
    def test_get_vehicle_brand_count(self,magasin_test):
        assert magasin_test.get_vehicle_brand_count("Toyota") == 2

    def test_add_vehicle(self,magasin_test, vehicule_test):
        magasin_test.add_vehicle(vehicule_test)
        assert magasin_test.inventory[-1] == vehicule_test
        assert magasin_test.stock["Toyota"] == 3

    def test_delete_vehicle(self,magasin_test, vehicule_test):
        magasin_test.delete_vehicle(Moto("T500","Dukati","Verte",25000,30))
        assert len(magasin_test.inventory) == 2
        assert magasin_test.stock["Dukati"] == 0
        with pytest.raises(ValueError):
            magasin_test.delete_vehicle(vehicule_test)

    def test_add_seller(self,magasin_test):
        magasin_test.add_seller("Denis",True)
        assert magasin_test.seller_list[-1] == Seller("Denis",magasin_test, senior=True)

    def test_delete_seller(self,magasin_test):
        len_magasin_init= len(magasin_test.seller_list)
        magasin_test.delete_seller(Seller("Robert",magasin_test, senior=False))
        assert len(magasin_test.seller_list) == len_magasin_init-1
        with pytest.raises(ValueError):
            magasin_test.delete_seller(Seller("Denis",magasin_test, senior=True))

@pytest.fixture
def seller_senior_test(magasin_test):
    return Seller("Fabien", magasin_test, senior=True)

@pytest.fixture
def seller_junior_test(magasin_test):
    return Seller("Fabien", magasin_test, senior=False)

@pytest.fixture
def client_test():
    return Client("Caroline","email",98)


class TestSeller:
    def test_create_sale(self,seller_senior_test, vehicule_test_in_store, client_test):
        # test du retour de la méthode
        assert seller_senior_test.create_sale(vehicule_test_in_store,client_test) == Vente(seller_senior_test.magasin,vehicule_test_in_store,seller_senior_test,client_test,False)
        
        # test de la modification des autres classes
        assert seller_senior_test.liste_de_vente[-1] == Vente(seller_senior_test.magasin,vehicule_test_in_store,seller_senior_test,client_test,False)
        assert Vente(seller_senior_test.magasin,vehicule_test_in_store,seller_senior_test,client_test,False) not in seller_senior_test.magasin.inventory

    def test_final_price_junior(self,seller_junior_test, vehicule_test_in_store, client_test):
        # test final price when junior
        assert seller_junior_test.create_sale(vehicule_test_in_store,client_test).reduction == False
        


@pytest.fixture
def vente_test(magasin_test,vehicule_test_in_store, seller_senior_test, client_test):
    return Vente(magasin_test,vehicule_test_in_store, seller_senior_test, client_test,True)

class TestVente:
    def test_create_pdf(self,tmpdir, vente_test):
        p = tmpdir.mkdir("tempdir")
        vente_test.create_pdf(path=p)
        assert os.path.exists(os.path.join(p,f'Facture_{vente_test.vehicule.marque}.pdf')) == True
        