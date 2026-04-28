import re

class CustomerValidator:
    def validate_phone(phone: str) -> bool:
        pattern = r'^[\+]?[0-9\s\-()]+$'
        phone_digits = re.sub(r'[^0-9]', '', phone)
        return len(phone_digits) >= 10 and re.match(pattern, phone) is not None
    
    def validate_name(name: str) -> bool:
        return len(name.strip()) >= 2 and len(name.strip()) <= 100
    
class CustomerProfile:
    def __init__(self, customer_id: str, name: str, 
                 phone: str):
        if not CustomerValidator.validate_name(name):
            raise ValueError("Invalid customer name")
        if not CustomerValidator.validate_phone(phone):
            raise ValueError("Invalid phone format")
        
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
    
    def update_phone(self, phone: str) -> None:
        if not CustomerValidator.validate_phone(phone):
            raise ValueError("Invalid phone format")
        self.phone = phone

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.accounts = []
        self.beneficiaries = []
    
    def authenticate(self, password: str) -> bool:
        return password == "1234"
    
    def view_statement(self, account_id: str) -> dict:
        return {"account_id": account_id, "balance": 100.0}
    
    def add_beneficiary(self, beneficiary_id: str) -> None:
        if beneficiary_id not in self.beneficiaries:
            self.beneficiaries.append(beneficiary_id)
    