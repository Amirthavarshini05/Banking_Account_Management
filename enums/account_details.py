from enum import Enum
class AuthenticationMethod(Enum):
    PIN = "pin"
    OTP = "otp"

class AccountType(Enum):
    SAVINGS = "Savings"
    CHECKING = "Checking"
    BUSINESS = "Business"

class AccountStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    FROZEN = "Frozen"