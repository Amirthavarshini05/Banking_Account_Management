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
    def __init__(
        self,
        account_id: str,
        customer_id: str,
        account_type: AccountType,
        initial_balance: float
    ):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = initial_balance
        self.status = AccountStatus.ACTIVE


class AccountService:
    def __init__(self, bank):
        self.bank = bank

    def create_account(
        self,
        customer_id: str,
        account_type: AccountType,
        initial_balance: float = 0.0
    ) -> Account:
        return self.bank.create_account(customer_id, account_type, initial_balance)

    def deposit(self, account_id: str, amount: float) -> None:
        account = self._get_valid_account(account_id)

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        account.balance += amount

    def withdraw(self, account_id: str, amount: float) -> None:
        account = self._get_valid_account(account_id)

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if account.balance < amount:
            raise InsufficientBalanceError("Insufficient balance")

        account.balance -= amount

    def get_balance(self, account_id: str) -> float:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError("Account does not exist")

        return self.bank.accounts[account_id].balance

    def freeze(self, account_id: str) -> None:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError("Account does not exist")

        account = self.bank.accounts[account_id]

        if account.status == AccountStatus.CLOSED:
            raise AccountClosedError("Cannot freeze closed account")

        account.status = AccountStatus.FROZEN

    def close(self, account_id: str) -> None:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError("Account does not exist")

        self.bank.accounts[account_id].status = AccountStatus.CLOSED

    def _get_valid_account(self, account_id: str) -> Account:
        if account_id not in self.bank.accounts:
            raise InvalidAccountError("Account does not exist")

        account = self.bank.accounts[account_id]

        if account.status == AccountStatus.CLOSED:
            raise AccountClosedError("Account is closed")

        if account.status == AccountStatus.FROZEN:
            raise AccountFrozenError("Account is frozen")

        return account