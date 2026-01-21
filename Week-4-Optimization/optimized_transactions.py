"""
Week 4: Optimization & Readability
Description:
Refactored transaction processing using modular
functions and basic validation.
"""

REQUIRED_FIELDS = {"sender", "receiver", "amount"}

def is_valid_transaction(transaction):
    return REQUIRED_FIELDS.issubset(transaction.keys())

def print_transaction(transaction):
    print(f"Sender   : {transaction['sender']}")
    print(f"Receiver : {transaction['receiver']}")
    print(f"Amount   : {transaction['amount']}")
    print("-" * 25)

def process_transactions(transactions):
    if not transactions:
        print("No transactions available.")
        return

    for tx in transactions:
        if is_valid_transaction(tx):
            print_transaction(tx)
        else:
            print("Invalid transaction detected.")

def main():
    transactions = [
        {"sender": "Alice", "receiver": "Bob", "amount": 50},
        {"sender": "Bob", "receiver": "Charlie", "amount": 30},
        {"sender": "Charlie", "receiver": "Dave", "amount": 20}
    ]
    process_transactions(transactions)

if __name__ == "__main__":
    main()
