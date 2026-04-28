from typing import TYPE_CHECKING
from enums.account_details import AccountType
from models.customer import Customer

if TYPE_CHECKING:
    from services.account import Account


class Bank:
    def __init__(self, bank_id: str, name: str):
        self.bank_id = bank_id
        self.name = name
        self.accounts = {}
        self.customers = {}

    def add_customer(self, customer: Customer) -> None:
        self.customers[customer.customer_id] = customer

    def create_account(
        self,
        customer_id: str,
        account_type: AccountType,
        initial_balance: float = 0.0
    ) -> "Account":

        from services.account import Account

        if customer_id not in self.customers:
            raise ValueError("Customer does not exist")

        customer_accounts = [
            account for account in self.accounts.values()
            if account.customer_id == customer_id
        ]

        account_id = f"ACC_{customer_id}_{len(customer_accounts) + 1:03d}"

        account = Account(account_id, customer_id, account_type, initial_balance)

        self.accounts[account_id] = account
        self.customers[customer_id].add_account(account_id)

        return account

    def calculate_interest(self, account_id: str) -> float:
        if account_id not in self.accounts:
            raise ValueError("Account does not exist")

        account = self.accounts[account_id]

        if account.account_type == AccountType.SAVINGS:
            return account.balance * 0.04

        return 0.0