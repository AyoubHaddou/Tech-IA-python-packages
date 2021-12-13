from dataclasses import dataclass
from concessionnaire.vehicule import Vehicule
from concessionnaire.client import Client
from fpdf import FPDF
import os

@dataclass
class Vente:
    magasin: "Magasin"
    vehicule : Vehicule
    vendeur : "Vendeur"
    client : Client
    reduction : bool

    def create_pdf(self,path=None):
        print(f"Facture au format PDF pour une {self.vehicule.marque} {self.vehicule.couleur} à {self.vehicule.final_price(self.reduction)} par {self.vendeur.full_name}")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 16)
        pdf.cell(60, 10, "Facture", 'C')
        pdf.ln(20)
        pdf.cell(60, 10, f"Voiture: {self.vehicule.marque} {self.vehicule.couleur} à {self.vehicule.final_price(self.reduction)} euros")
        pdf.ln(20)
        pdf.cell(60, 10, f"Vendeur: {self.vendeur.full_name}")
        file_path = f'Facture_{self.vehicule.marque}.pdf'
        if path:
            final_path = os.path.join(path,file_path)
            pdf.output(final_path, 'F')
        else:
            pdf.output(file_path, 'F')
