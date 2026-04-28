from services.account import InvalidAccountError


class MiniStatementService:
    def __init__(self, bank, account_service, transaction_service):
        self.bank = bank
        self.account_service = account_service
        self.transaction_service = transaction_service

    def get_mini_statement(self, account_id: str, limit: int = 5) -> dict:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError("Account does not exist")

        account = self.bank.accounts[account_id]
        customer = self.bank.customers.get(account.customer_id)

        customer_name = customer.name if customer else account.customer_id

        transactions = self.transaction_service.get_account_transactions(account_id)

        recent_transactions = sorted(
            transactions,
            key=lambda transaction: transaction.timestamp,
            reverse=True
        )[:limit]

        return {
            "account_details": {
                "account_id": account.account_id,
                "customer_name": customer_name,
                "account_type": account.account_type.value,
                "balance": account.balance,
                "status": account.status.value
            },
            "transactions": [
                {
                    "transaction_id": transaction.transaction_id,
                    "type": transaction.transaction_type,
                    "amount": transaction.amount,
                    "description": transaction.description,
                    "timestamp": transaction.timestamp.isoformat()
                }
                for transaction in recent_transactions
            ],
            "transaction_count": len(recent_transactions)
        }