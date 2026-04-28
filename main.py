from models.bank import Bank
from models.customer import Customer
from enums.account_details import AccountType
from services.account import AccountService
from services.transaction import TransactionService
from services.mini_statement import MiniStatementService


def print_statement(statement: dict):
    account = statement["account_details"]

    print(f"  Customer Name: {account['customer_name']}")
    print(f"  Account ID: {account['account_id']}")
    print(f"  Account Type: {account['account_type']}")
    print(f"  Balance: ₹{account['balance']}")
    print(f"  Status: {account['status']}")
    print(f"  Recent Transactions: {statement['transaction_count']}")

    if statement["transaction_count"] == 0:
        print("    No transactions found")
    else:
        for transaction in statement["transactions"]:
            print(
                f"    {transaction['type']} | "
                f"₹{transaction['amount']} | "
                f"{transaction['description']} | "
                f"{transaction['timestamp']}"
            )


def print_bank_summary(bank, transaction_service):
    transactions = transaction_service.transactions

    total_deposits = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "DEPOSIT"
    )

    total_withdrawals = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "WITHDRAWAL"
    )

    total_transfers = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "TRANSFER"
    )

    print("\n=== Bank Summary ===")
    print(f"Bank Name: {bank.name}")
    print(f"Bank ID: {bank.bank_id}")
    print(f"Total Customers: {len(bank.customers)}")
    print(f"Total Accounts: {len(bank.accounts)}")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Deposits: ₹{total_deposits}")
    print(f"Total Withdrawals: ₹{total_withdrawals}")
    print(f"Total Transfers: ₹{total_transfers}")


def main():
    print("Banking Account Management\n")

    bank = Bank("BANK001", "Demo Bank")

    account_service = AccountService(bank)
    transaction_service = TransactionService(bank, account_service)
    statement_service = MiniStatementService(
        bank,
        account_service,
        transaction_service
    )

    customer1 = Customer(
        "CUST001",
        "John Doe",
        "john.doe@email.com",
        "+1234567890",
        "123 Main Street"
    )

    customer2 = Customer(
        "CUST002",
        "Jane Smith",
        "jane.smith@email.com",
        "+1987654321",
        "456 Oak Avenue"
    )

    bank.add_customer(customer1)
    bank.add_customer(customer2)

    account1 = account_service.create_account(
        "CUST001",
        AccountType.SAVINGS,
        1000.0
    )

    account2 = account_service.create_account(
        "CUST001",
        AccountType.CHECKING,
        500.0
    )

    account3 = account_service.create_account(
        "CUST002",
        AccountType.SAVINGS,
        2000.0
    )

    print("Accounts created successfully\n")

    print("Performing transactions...\n")

    transaction_service.deposit(
        account1.account_id,
        500.0,
        "Salary deposit"
    )

    transaction_service.deposit(
        account3.account_id,
        1000.0,
        "Business income"
    )

    transaction_service.withdraw(
        account2.account_id,
        200.0,
        "Grocery shopping"
    )

    transaction_service.withdraw(
        account1.account_id,
        100.0,
        "ATM withdrawal"
    )

    transaction_service.transfer(
        account1.account_id,
        account2.account_id,
        300.0,
        "Transfer to checking account"
    )

    print("Transactions completed successfully")

    print("\n=== Mini Statements ===")

    print(f"\nMini Statement for {account1.account_id}:")
    statement1 = statement_service.get_mini_statement(account1.account_id, 5)
    print_statement(statement1)

    print(f"\nMini Statement for {account2.account_id}:")
    statement2 = statement_service.get_mini_statement(account2.account_id, 5)
    print_statement(statement2)

    print(f"\nMini Statement for {account3.account_id}:")
    statement3 = statement_service.get_mini_statement(account3.account_id, 5)
    print_statement(statement3)

    print_bank_summary(bank, transaction_service)


if __name__ == "__main__":
    main()