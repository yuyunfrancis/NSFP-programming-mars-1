from __future__ import annotations

import json
from datetime import datetime

from typing import List
from .sale import Sale

class BookRecords:
    """A record of all the sales made through the application.
    
    Attributes:
        transactions: a list of the transactions
    """
    def __init__(self, transactions: List[Sale]) -> None:
        self.transactions = transactions
    
    def __str__(self) -> str:
        """Returns a string representation of a record.
        
        Args:
        
        Returns: A string
        """

        #TODO: In the format below, return a representation of the records
        # |      # | Date                | Customer   | Medication | Quantity | Purchase Price | Prescription |
        # |      1 | 2023-06-03 21:23:25 | doe        | Quinine    |        3 |       1400 RWF | PHA1         |

        print(f"|\t#|Date\t|Customer\t|Medication\t|Quantity\t|Purchase Price\t|Prescription\t|")
        for i,transaction in enumerate(self.transactions):
            print(f"|\t{i+1}|{transaction.timestamp}\t|{transaction.customerID}\t|{transaction.name}\t|{transaction.quantity}\t|{transaction.purchase_price}\t|{transaction.prescriptionID}\t|")
    
    def reportOnPrescriptions(self) -> str:
        """Reports on prescription sales.

        Args: 

        Returns: A string report of the prescriptions processed
        """
        #TODO: From the transactions data, retrieve for each prescription, the actual medications that were processed
        # and aggregate for each, the corresponding total price.

        #TODO: output in the following format, the results: 
        # |    # | Prescription ID | Total Price |
        
        print(f"|\t#|Prescription ID\t|Total Price\t|")
        for i,transaction in enumerate(self.transactions):
            print(f"|\t{i+1}|{transaction.prescriptionID}\t|{transaction.purchase_price}\t|")

    def purchasesByUser(self, customerID: str):
        """Reports on the sales performed by a customer.
        
        Args:
            customerID: Username of the customer.

        Returns: A string representation of the corresponding transactions
            
        """
        #TODO: Query the transactions to the `transactions` list below
        transactions = [transaction for transaction in self.transactions if transaction.customerID == customerID]

        return BookRecords(transactions).__str__()

    def salesByAgent(self, salesperson: str):
        """Reports on the sales performed by a pharmacist.
        
        Args:
            salesperson: Username of the pharmacist.

        Returns: A string representation of the corresponding transactions
            
        """
        #TODO: Query the transactions to the `transactions` list below
        transactions = [transaction for transaction in self.transactions if transaction.salesperson == salesperson]
        

        # return the string representation
        return BookRecords(transactions).__str__()
    
    def topNSales(self, start: datetime = datetime.strptime('1970-01-02', '%Y-%m-%d'), end: datetime = datetime.now(), n = 10) -> str:
        """Return the top n sales ordered by the total price of purchases.

        Args:
            start: a datetime representing the start period to consider (datetime, default to 01 Jan 1970)
            end: a datetime representing the end period to consider (datetime, default to current timestamp)
            n: number of records to consider (int, default to 10)

        Returns:
        A string representation of the top n 
        """
        #TODO: Query the top transactions and save them to the variable `transactions` below
        transactions = None
        for transaction in self.transactions:
            date_start = datetime.strptime(start, '%Y-%m-%d')
            date_end = datetime.strptime(end, '%Y-%m-%d')
            timestamp_start = int((date_start - datetime(1970, 1, 1)).total_seconds())
            timestamp_end = int((date_end - datetime(1970, 1, 1)).total_seconds())

            if transaction.timestamp >= timestamp_start and transaction.timestamp <= timestamp_end:
                transactions.append(transaction)    

        sorted_trans = sorted(transactions, key=lambda transaction: transaction.purchase_price)
        sorted_trans = sorted_trans[:n]
        # return the string representation of the transactions.
        return BookRecords(transactions).__str__()


    def totalTransactions(self) -> float:
        """Returns the total cost of the transactions considered.
        
        Args:
        
        Returns: A floating number representing the total price
        """
        return sum([transaction.purchase_price for transaction in self.transactions])
    
    @classmethod
    def load(cls, infile: str) -> BookRecords:
        """Loads a JSON file containing a number of sales object
        
        Args:
            infile: path to the file to be read
        Returns: A new object with the transactions in the file
        """
        #TODO: Implement the function. Make sure to handle the cases where
        # the file does not exist.
        try:
            with open(infile, 'r') as file:
                data=json.load(file)
                transactions = [Sale(transaction["id"], transaction["name"], transaction["quantity"], transaction["price"], transaction["purchase_price"], transaction["timestamp"], transaction["customerID"], transaction["salesperson"], transaction["prescriptionID"]) for transaction in data]
                return BookRecords(transactions)
        except IOError:
            print("File not found!!")