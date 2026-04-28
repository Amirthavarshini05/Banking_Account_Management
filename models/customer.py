import re


class CustomerValidator:

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r'^[\+]?[0-9\s\-()]+$'
        phone_digits = re.sub(r'[^0-9]', '', phone)
        return len(phone_digits) >= 10 and re.match(pattern, phone) is not None

    @staticmethod
    def validate_name(name: str) -> bool:
        return 2 <= len(name.strip()) <= 100


class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str):
        if not CustomerValidator.validate_name(name):
            raise ValueError("Invalid customer name")

        if not CustomerValidator.validate_phone(phone):
            raise ValueError("Invalid phone format")

        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.accounts = []
        self.beneficiaries = []

    def authenticate(self, password: str) -> bool:
        return password == "1234"

    def add_account(self, account_id: str) -> None:
        if account_id not in self.accounts:
            self.accounts.append(account_id)

    def view_statement(self, account_id: str) -> dict:
        return {
            "account_id": account_id,
            "message": "Statement generated"
        }

    def add_beneficiary(self, beneficiary_id: str) -> None:
        if beneficiary_id not in self.beneficiaries:
            self.beneficiaries.append(beneficiary_id)