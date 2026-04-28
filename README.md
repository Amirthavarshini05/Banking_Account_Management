<h1 align="left">Banking Account Management System</h1>

###

<h2 align="left">Problem Statement</h2>

###

<p align="left">Managing banking operations manually or without a structured system can lead to errors, inefficiency, and lack of scalability. Basic operations such as account creation, deposits, withdrawals, transfers, and transaction tracking require a well-organized system.<br><br>This project aims to build a modular and object-oriented Banking Account Management System using Python that:<br><br>Manages customers and their accounts<br>Supports multiple account types (Savings, Checking, Business)<br>Handles transactions (Deposit, Withdrawal, Transfer)<br>Generates mini statements<br>Maintains transaction history</p>

###

<h2 align="left">Approach</h2>

###

<p align="left">The system is designed using Object-Oriented Programming (OOP) principles and follows a layered architecture:</p>

###

<h3 align="left">1. Modular Structure</h3>

###

<p align="left">The project is divided into:<br><br>models → Core entities (Bank, Customer)<br>services → Business logic (Account, Transaction, Statement)<br>enums → Fixed constants (AccountType, Status)</p>

###

<h3 align="left">2. Core Logic</h3>

###

<h4 align="left">Bank Management</h4>

###

<p align="left">Stores all customers and accounts<br>Responsible for account creation<br>Generates unique Account IDs</p>

###

<h4 align="left">Account Handling</h4>

###

<p align="left">Each account has:<br>ID<br>Type<br>Balance<br>Status (Active / Frozen / Closed)<br>Validations include:<br>Cannot withdraw more than balance<br>Cannot operate on frozen/closed accounts</p>

###

<h4 align="left">Transaction Processing</h4>

###

<p align="left">Supports:<br>Deposit<br>Withdrawal<br>Transfer<br>Each transaction:<br>Has unique ID (UUID)<br>Stores timestamp<br>Maintains history</p>

###

<h4 align="left">Mini Statement Generation</h4>

###

<p align="left">Fetches recent transactions<br>Sorts by latest timestamp<br>Displays limited records (e.g., last 5 transactions)</p>

###

<h4 align="left">Exception Handling</h4>

###

<p align="left">Custom exceptions are used for safety:<br><br>InvalidAccountError<br>InsufficientBalanceError<br>AccountFrozenError<br>AccountClosedError</p>

###

<p align="left">3. Design Principles Used</p>

###

<p align="left">Encapsulation (data + methods inside classes)<br>Separation of Concerns (models vs services)<br>Reusability (services reused across modules)<br>Scalability (easy to extend with new features)</p>

###

<p align="left"></p>

###

<h2 align="left">Steps to Execute the Code</h2>

###

<p align="left">Step 1: Clone or Download Project<br>git clone <your-repo-link><br>cd Banking_Account_Management<br><br>Step 2: Verify Folder Structure<br>Banking_Account_Management/<br>│<br>├── main.py<br>├── enums/<br>├── models/<br>└── services/<br><br>Make sure each folder contains __init__.py.<br><br>Step 3: Run the Application<br>python main.py<br><br>Step 4: Output</p>

###

<h2 align="left">Output</h2>

###

<p align="left">The program will:<br><br>Initialize the bank<br>Create customers and accounts<br>Perform transactions:<br>Deposit<br>Withdrawal<br>Transfer<br>Display:<br>Mini statements<br>Bank summary</p>

###

<h2 align="left">Sample Features Demonstrated</h2>

###

<p align="left">1. Create accounts<br>2. Deposit & Withdraw money<br>3. Transfer funds between accounts<br>4. View mini statement<br>5. Track transaction history<br>6. Handle errors safely</p>

###

<h2 align="left">Author</h2>

###

<p align="left">Amirthavarshini R U<br>230701027<br>Computer Science Engineering Student</p>

###
