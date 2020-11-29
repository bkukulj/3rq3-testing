from dinnerisserved.creditcards import CreditCards

def test_credit_card_verifies_expiry_date():
    valid_dates = [
        "11/24",
        "09/26",
        "01/22",
    ]

    creditcard = CreditCards()
    for date in valid_dates:
        assert creditcard.verify_expdate(date) == True, "date should be verified as valid"


def test_credit_card_fails_invalid_dates():
    invalid_dates = [
        "26/13",
        "aaaaa",
        None
    ]

    creditcard = CreditCards()
    for date in invalid_dates:
        assert creditcard.verify_expdate(date) == False, "date should not be verified, it is false"
