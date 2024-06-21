def bank_transaction() -> int:
    balance = 0
    while True:
        transaction = input()
        if not transaction:
            break
        transaction = transaction.split()
        if transaction[0] == 'D':
            balance += int(transaction[1])
        elif transaction[0] == 'W':
            balance -= int(transaction[1])
    return balance


if __name__ == '__main__':
    print(bank_transaction())