from datetime import datetime
from typing import List
import uuid

from services.account import InsufficientBalanceError


class Transaction:
    def __init__(
        self,
        transaction_id: str,
        transaction_type: str,
        amount: float,
        description: str,
        timestamp: datetime = None,
        account_id: str = None,
        from_account_id: str = None,
        to_account_id: str = None
    ):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = timestamp or datetime.now()
        self.account_id = account_id
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id


class TransactionException(Exception):
    pass


class InvalidTransactionError(TransactionException):
    pass


class TransactionService:
    def __init__(self, bank, account_service):
        self.bank = bank
        self.account_service = account_service
        self.transactions = []

    def _record_transaction(
        self,
        transaction_type: str,
        amount: float,
        description: str,
        account_id: str = None,
        from_account_id: str = None,
        to_account_id: str = None
    ) -> Transaction:

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            transaction_type=transaction_type,
            amount=amount,
            description=description,
            account_id=account_id,
            from_account_id=from_account_id,
            to_account_id=to_account_id
        )

        self.transactions.append(transaction)
        return transaction

    def deposit(self, account_id: str, amount: float, description: str) -> Transaction:
        self.account_service.deposit(account_id, amount)

        return self._record_transaction(
            "DEPOSIT",
            amount,
            description,
            account_id=account_id
        )

    def withdraw(self, account_id: str, amount: float, description: str) -> Transaction:
        self.account_service.withdraw(account_id, amount)

        return self._record_transaction(
            "WITHDRAWAL",
            amount,
            description,
            account_id=account_id
        )

    def transfer(
        self,
        from_account_id: str,
        to_account_id: str,
        amount: float,
        description: str
    ) -> Transaction:

        if amount <= 0:
            raise InvalidTransactionError("Transfer amount must be positive")

        if from_account_id == to_account_id:
            raise InvalidTransactionError("Cannot transfer to same account")

        balance = self.account_service.get_balance(from_account_id)

        if balance < amount:
            raise InsufficientBalanceError("Insufficient balance for transfer")

        self.account_service.withdraw(from_account_id, amount)
        self.account_service.deposit(to_account_id, amount)

        return self._record_transaction(
            "TRANSFER",
            amount,
            description,
            from_account_id=from_account_id,
            to_account_id=to_account_id
        )

    def get_account_transactions(self, account_id: str) -> List[Transaction]:
        return [
            transaction for transaction in self.transactions
            if transaction.account_id == account_id
            or transaction.from_account_id == account_id
            or transaction.to_account_id == account_id
        ]

    def get_receipt(self, transaction_id: str) -> dict:
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return {
                    "transaction_id": transaction.transaction_id,
                    "type": transaction.transaction_type,
                    "amount": transaction.amount,
                    "description": transaction.description,
                    "timestamp": transaction.timestamp.isoformat(),
                    "status": "Completed"
                }

        return {
            "transaction_id": transaction_id,
            "status": "Not Found"
        }