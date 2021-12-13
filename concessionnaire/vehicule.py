"""définit la classe véhicule et ses sous classes: Auto, Moto, Camion"""

from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta

@dataclass
class Vehicule(metaclass = ABCMeta):
    modele : str
    marque :str
    couleur :str
    prix_HT :int
    reduction :int
    _prix_TTC: float = field(init=False)
  

    def __post_init__(self):
        self._prix_TTC : float = self._get_prix_TTC()

    @property
    def prix_TTC(self) -> float:
        return self._prix_TTC

    @property
    def reduction(self) -> int:
        return self._reduction

    @reduction.setter
    def reduction(self, value):
        if not isinstance(value,int) :
            raise ValueError("Reduction should be an int")
        elif value > 100 or value < 0:
            raise ValueError("Reduction should be between 0 et 100")
        else:
            self._reduction = value

    @property
    def prix_HT(self) -> int:
        return self._prix_HT   


    @prix_HT.setter
    def prix_HT(self, value):
        if not isinstance(value,int):
            raise ValueError("Prix should be an integer")
        else:
            self._prix_HT = value
            self._prix_TTC = self._get_prix_TTC()

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, value):
        if not isinstance(value,str):
            raise ValueError("Marque should be a str")
        else:
            self._marque = value

    @property
    def couleur(self) -> str:
        return self._couleur

    @couleur.setter
    def couleur(self, value):
        if not isinstance(value,str):
            raise ValueError("Couleur should be a str")
        else:
            self._couleur = value

    def _get_prix_TTC(self):
        return self.prix_HT * 1.2

    def final_price(self,reduction:bool):
        if reduction:
            return self.prix_TTC * (1 - self.reduction/100)
        else:
            return self.prix_TTC


@dataclass
class Voiture(Vehicule):
    roues : ClassVar[int] = 4
    type : ClassVar[str] = "Voiture"

@dataclass
class Moto(Vehicule):
    roues : ClassVar[int] = 2
    type : ClassVar[str] = "Moto"
  


@dataclass
class Camion(Vehicule):
    roues : ClassVar[int]
    type : ClassVar[str] = "Camion"
