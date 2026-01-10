def bank_details(name, acc_no, balance, branch):
    result = (
        f"Account Holder Name: {name}\n"
        f"Account Number: {acc_no}\n"
        f"Balance: {balance}\n"
        f"Branch: {branch}"
    )
    return result


if __name__ == "__main__":
    name = "Ammu"
    acc_no = "ACC1001"
    balance = 5000
    branch = "Pune"

    print(bank_details(name, acc_no, balance, branch))
