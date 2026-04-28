from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
import uuid

if TYPE_CHECKING:
    from models.bank import Bank
from models.customer import Customer
from enums.account_details import AccountStatus, AccountType

class AccountException(Exception):
    pass

class InvalidAccountError(AccountException):
    pass

class InsufficientBalanceError(AccountException):
    pass


class AccountFrozenError(AccountException):
    pass


class AccountClosedError(AccountException):
    pass

class Account:
    def __init__(self, account_id: str, customer_id: str, account_type: AccountType, initial_balance: float):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = initial_balance
        self.status = AccountStatus.ACTIVE

class AccountService:
    def __init__(self, bank: "Bank"):
        self.bank = bank
    
    def create_account(self, customer_id: str, account_type: AccountType, initial_balance: float = 0.0) -> Account:
        return self.bank.create_account(customer_id, account_type, initial_balance)
    
    def deposit(self, account_id: str, amount: float) -> None:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError(f"Account {account_id} does not exist")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        account = self.bank.accounts[account_id]
        if account.status == AccountStatus.CLOSED:
            raise AccountClosedError("Cannot deposit to closed account")
        if account.status == AccountStatus.FROZEN:
            raise AccountFrozenError("Cannot deposit to frozen account")
        account.balance += amount
    
    def withdraw(self, account_id: str, amount: float) -> None:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError(f"Account {account_id} does not exist")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        account = self.bank.accounts[account_id]
        if account.status == AccountStatus.CLOSED:
            raise AccountClosedError("Cannot withdraw from closed account")
        if account.status == AccountStatus.FROZEN:
            raise AccountFrozenError("Cannot withdraw from frozen account")
        if account.balance < amount:
            raise InsufficientBalanceError("Insufficient balance")
        account.balance -= amount
    
    def get_balance(self, account_id: str) -> float:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError(f"Account {account_id} does not exist")
        account = self.bank.accounts[account_id]
        return account.balance
    
    def freeze(self, account_id: str) -> None:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError(f"Account {account_id} does not exist")
        account = self.bank.accounts[account_id]
        if account.status == AccountStatus.CLOSED:
            raise AccountClosedError("Cannot freeze closed account")
        account.status = AccountStatus.FROZEN
