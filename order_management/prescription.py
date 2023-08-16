import json

from typing import List, Dict, Union
from .product import Product


class Prescription:
    def __init__(self, DoctorName: str, PrescriptionID: str, Medications: List[Dict[str, Union[int, str, bool]]],
                 CustomerID: str, Date: str) -> None:
        self.DoctorName = DoctorName
        self.PrescriptionID = PrescriptionID
        self.Medications = Medications
        self.CustomerID = CustomerID

    def medecineInPrescription(self, product: Product, quantity: int) -> bool:
        for medication in self.Medications:
            if (
                    medication["id"] == product.code
                    and medication["quantity"] >= quantity
            ):
                return True
        return False

    def markComplete(self, product: Product):
        for medication in self.Medications:
            if medication["id"] == product.code:
                medication["ProcessedStatus"] = True
                break


    def dump(self, outfile: str):
        """Dumps the updated prescription to the specified file

        Args:
            outfile: path to the file where the output should be written

        Returns: None
        """
        #TODO: Read the output file (safely).

        #TODO: Update the prescription that is being edited in the loaded data

        #TODO: Save the updated object
    
    @classmethod
    def get(cls, infile: str, id: str):

        try:
            with open(infile, 'r') as file:
                prescriptions = json.load(file)
        except FileNotFoundError:
            prescriptions = []

        for prescription in prescriptions:
            if prescription["PrescriptionID"] == id:
                return prescription

        return None

