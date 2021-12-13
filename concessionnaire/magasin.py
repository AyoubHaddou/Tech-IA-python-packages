from dataclasses import dataclass, field
from concessionnaire.seller import Seller


@dataclass
class Magasin():
    adresse: str 
    siret: str
    _seller_list: list = field(default_factory=list)
    _inventory: list = field(default_factory=list)
    _stock: dict = field(default_factory=dict)
    
        
    @property
    def seller_list(self) -> list:
        return self._seller_list
    
        
    @property
    def inventory(self) -> list:
        return self._inventory

        
    @property
    def stock(self) -> dict:
        return self._stock
    
        
        
    def get_vehicle_brand_count(self, marque):
        return self._stock[marque]

    
    def add_vehicle(self, vehicle):
        self._inventory.append(vehicle)
        if vehicle.marque not in self.stock:
            self._stock[vehicle.marque] = 0
        self._stock[vehicle.marque] += 1
        print(f"la {vehicle.marque} a été ajoutée à l'inventaire")
        return self._inventory
    
    def delete_vehicle(self, vehicle):
        self._inventory.remove(vehicle)
        self._stock[vehicle.marque] -= 1
        print(f"la {vehicle.marque} a été retirée de l'inventaire")
        return self.inventory
    
    def add_seller(self, full_name:str, senior:bool):
        seller = Seller(full_name,self,senior=senior)
        self._seller_list.append(seller)
        print(f"le vendeur {seller.full_name} a été recruté")
        return self._seller_list
    
    def delete_seller(self, seller):
        self._seller_list.remove(seller)
        print(f"le vendeur {seller.full_name} a été supprimé du magasin")
        return self._seller_list

# @dataclass
# class Seller():
#     full_name: str
#     _magasin: Magasin
#     _liste_de_vente: list = field(default_factory=list)
#     senior: bool = False

#     @property
#     def liste_de_vente(self) -> list:
#         return self._liste_de_vente

#     @property
#     def magasin(self) -> Magasin:
#         return self._magasin

#     def create_sale(self,vehicule,client,reduction_asked=False):
#         if reduction_asked & self.senior:
#             sale = Vente(self._magasin,vehicule,self,client,True)
#         else:
#             sale = Vente(self._magasin,vehicule,self,client,False)
#         self._liste_de_vente.append(sale)
#         self._magasin.delete_vehicle(vehicule)
#         return sale