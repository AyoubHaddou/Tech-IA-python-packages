
from concessionnaire.vehicule import Voiture
from concessionnaire.magasin import Magasin
from concessionnaire.seller import Seller
from concessionnaire.client import Client



mon_magasin = Magasin("Rue Barthelemy Delespaul","084948384")
my_seller = Seller("Denis",mon_magasin, senior=True)
my_car = Voiture("Hiaris","Toyota","Rouge",10000, 20)
my_client = Client("Fabien","fb",89)

mon_magasin.add_vehicle(my_car)
mon_magasin.add_seller("Denis",True)

my_sale = mon_magasin._seller_list[0].create_sale( my_car, my_client,True)
print(my_sale)
print(mon_magasin.inventory)


