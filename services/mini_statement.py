from typing import List, Optional
from datetime import datetime, timedelta

from models.bank import Bank
from services.account import AccountService, InvalidAccountError
from services.transaction import TransactionService


class MiniStatementService:

    def __init__(self, bank: Bank, account_service: AccountService,
                 transaction_service: TransactionService):
        self.bank = bank
        self.account_service = account_service
        self.transaction_service = transaction_service
    
    def generate(self, account_id: str) -> dict:
        return {"account_id": account_id, "transactions": []}

    def get_mini_statement(self, account_id: str, limit: int = 5) -> dict:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError(f"Account {account_id} does not exist")

        account = self.bank.accounts[account_id]
        customer = self.bank.customers.get(account.customer_id)
        customer_name = customer.name if customer else account.customer_id

        transactions = self.transaction_service.get_account_transactions(account_id)
        recent_transactions = sorted(transactions, key=lambda tx: tx.timestamp, reverse=True)[:limit]

        return {
            "account_details": {
                "account_id": account.account_id,
                "customer_name": customer_name,
                "account_type": account.account_type.value if hasattr(account.account_type, 'value') else str(account.account_type),
                "balance": account.balance,
                "status": account.status.value if hasattr(account.status, 'value') else str(account.status),
            },
            "transactions": [
                {
                    "transaction_id": tx.transaction_id,
                    "type": tx.transaction_type,
                    "amount": tx.amount,
                    "description": tx.description,
                    "timestamp": tx.timestamp.isoformat(),
                }
                for tx in recent_transactions
            ],
            "transaction_count": len(recent_transactions)
        }
    
    def filter_by_date(self, account_id: str, start_date: datetime, end_date: datetime) -> List[dict]:
        return []
    
    def export_to_pdf(self, account_id: str) -> str:
        return "PDF content"
