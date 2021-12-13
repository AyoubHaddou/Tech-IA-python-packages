from dataclasses import dataclass, field
from concessionnaire.vente import Vente

@dataclass
class Seller():
    full_name: str
    _magasin: "Magasin"
    _liste_de_vente: list = field(default_factory=list)
    senior: bool = False

    @property
    def liste_de_vente(self) -> list:
        return self._liste_de_vente

    @property
    def magasin(self) -> "Magasin":
        return self._magasin

    def create_sale(self,vehicule,client,reduction_asked=False):
        if reduction_asked & self.senior:
            sale = Vente(self._magasin,vehicule,self,client,True)
        else:
            sale = Vente(self._magasin,vehicule,self,client,False)
        self._liste_de_vente.append(sale)
        self._magasin.delete_vehicle(vehicule)
        return sale


