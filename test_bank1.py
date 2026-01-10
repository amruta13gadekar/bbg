from bank1 import bank_details


def test_bank_details():
    expected_output = (
        "Account Holder Name:Ammu\n"
        "Account Number:ACC1001\n"
        "Balance:5000\n"
        "Branch:Pune"
    )
    assert bank_details("Ammu", "ACC1001", 5000, "Pune") == expected_output
