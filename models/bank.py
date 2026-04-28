from enums.account_details import AccountType
from typing import TYPE_CHECKING
from models.customer import Customer

if TYPE_CHECKING:
    from services.account import Account

class Bank:
    def __init__(self, bank_id: str, name: str):
        self.bank_id = bank_id
        self.name = name
        self.accounts = {}
        self.customers = {}
    
    def create_account(self, customer_id: str, account_type: AccountType, initial_balance: float = 0.0) -> "Account":
        from services.account import Account

        account_id = f"ACC_{customer_id}_{len([a for a in self.accounts.values() if a.customer_id == customer_id]) + 1:03d}"
        account = Account(account_id, customer_id, account_type, initial_balance)
        self.accounts[account_id] = account
        return account
    
    def add_customer(self, customer: Customer) -> None:
        self.customers[customer.customer_id] = customer
    
    def calculate_interest(self, account_id: str) -> float:
        return 0.0
