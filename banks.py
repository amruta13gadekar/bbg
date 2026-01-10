def bank_account(name, acc_no, balance):
    if balance < 1000:
        status = "Low Balance"
    else:
        status = "Balance OK"

    return {
        "name": name,
        "account": acc_no,
        "balance": balance,
        "status": status
    }


def main():
    name = input("Enter name: ")
    acc_no = input("Enter account number: ")
    balance = int(input("Enter balance: "))

    result = bank_account(name, acc_no, balance)

    print("\nBank Account Details")
    print("Name:", result["name"])
    print("Account:", result["account"])
    print("Balance:", result["balance"])
    print("Status:", result["status"])


if __name__ == "__main__":
    main()
