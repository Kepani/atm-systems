# ATM System (Python)

A simplified ATM system built in Python to demonstrate clean architecture,
object-oriented design, and state-based workflows.

This project is designed as a **learning + interview-ready system design project**.

---

## Features (Current)
- ATM state machine (Idle → Card Inserted → Authenticated)
- User session handling
- PIN authentication
- Mock bank service
- Clean project structure

---

## Project Structure
atm-system/
├── atm/
│ ├── atm.py # ATM controller
│ ├── session.py # User session tracking
│ ├── states.py # ATM state machine
│ ├── services/
│ │ └── mock_bank.py # Mock bank backend
│ ├── transactions/ # Transaction logic (WIP)
│ └── hardware/ # ATM hardware simulation (WIP)
├── tests/
├── main.py # Entry point
├── requirements.txt
└── README.md

## Planned Features
- Withdraw / Deposit transactions
- Transaction factory & strategy pattern
- Cash dispenser simulation
- Receipt printing
- Error handling & edge cases
- Unit tests (pytest)