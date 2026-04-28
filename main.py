from models.bank import Bank
from models.customer import Customer
from enums.account_details import AccountType
from services.account import AccountService
from services.transaction import TransactionService
from services.mini_statement import MiniStatementService
from datetime import datetime, timedelta


def main():
    print("Banking Account Management/n")

    bank = Bank("BANK001", "Demo Bank")
    print(f"Initialized {bank.name} ({bank.bank_id})\n")

    account_service = AccountService(bank)
    transaction_service = TransactionService(bank, account_service)
    statement_service = MiniStatementService(bank, account_service, transaction_service)

    customer1 = Customer("CUST001", "John Doe", "john.doe@email.com", "+1234567890", "123 Main St")
    customer2 = Customer("CUST002", "Jane Smith", "jane.smith@email.com", "+1987654321", "456 Oak Ave")

    bank.add_customer(customer1)
    bank.add_customer(customer2)
    account1 = account_service.create_account("CUST001", AccountType.SAVINGS, 1000.0)
    account2 = account_service.create_account("CUST001", AccountType.CHECKING, 500.0)
    account3 = account_service.create_account("CUST002", AccountType.SAVINGS, 2000.0)

    print("Performing transactions...")

    
    #print("Deposits:")
    txn1 = transaction_service.deposit(account1.account_id, 500.0, "Salary deposit")
    txn2 = transaction_service.deposit(account3.account_id, 1000.0, "Business income")

  
    #print("\nWithdrawals:")
    txn3 = transaction_service.withdraw(account2.account_id, 200.0, "Grocery shopping")
    txn4 = transaction_service.withdraw(account1.account_id, 100.0, "ATM withdrawal")


    #print("\nTransfer:")
    txn5 = transaction_service.transfer(account1.account_id, account2.account_id, 300.0, "Transfer to checking")

    print()

    print("=== Mini Statements ===")

    print(f"\nMini Statement for {account1.account_id}:")
    stmt1 = statement_service.get_mini_statement(account1.account_id, 3)
    print_statement(stmt1)

    print(f"\nMini Statement for {account2.account_id}:")
    stmt2 = statement_service.get_mini_statement(account2.account_id, 3)
    print_statement(stmt2)

    print(f"\nMini Statement for {account3.account_id}:")
    stmt3 = statement_service.get_mini_statement(account3.account_id, 3)
    print_statement(stmt3)

   
    print("\n=== Bank Summary ===")
    summary = bank.get_bank_summary()
    print(f"Bank: {summary['bank_name']}")
    print(f"Total Customers: {summary['total_customers']}")
    print(f"Total Accounts: {summary['total_accounts']}")
    print(f"Total Transactions: {summary['total_transactions']}")
    print(f"Total Deposits: ${summary['total_deposits']:.2f}")
    print(f"Total Withdrawals: ${summary['total_withdrawals']:.2f}")

def print_statement(statement: dict):
    account = statement['account_details']
    print(f"  Customer: {account['customer_name']}")
    print(f"  Account Type: {account['account_type']}")
    print(f"  Current Balance: ${account['balance']}")
    print(f"  Status: {account['status']}")
    print(f"  Recent Transactions ({statement['transaction_count']}):")


if __name__ == "__main__":
    main()