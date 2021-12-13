from dataclasses import dataclass


@dataclass
class Client:
    nom : str
    email : str
    id : int