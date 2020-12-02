from dinnerisserved.visatest import VisaTest
from dinnerisserved.itemavailabilitytest import ItemAvailable
from dinnerisserved.customerprofiletest import CustomerProfile
from dinnerisserved.itemsorderstest import OrdersItems
from dinnerisserved.menuitems import MenuItem
from dinnerisserved.deliveryfee import DeliveryFee
#test 1
def test_credit_transation_status():
    visatest = VisaTest()
    checkexp=visatest.transaction_passed
    assert checkexp==True, "The visa transaction has passed"
#test 2
def test_credit_card_number():
    creditnumber = VisaTest()
    checknumber=creditnumber.valid_number
    assert checknumber==True, "The visa number entered is valid"
#test 3
def test_credit_ccv_number():
    ccv = VisaTest()
    checkccv=ccv.ccv_number
    assert checkccv==True, "The transaction is entered correctly"
#test 4
def test_credit_card_expiry():
    expiry = VisaTest()
    checkexiry=expiry.expiry_date
    assert checkexiry==True, "The expiry date is entered correctly"
#test 5
def test_breakfast_item():
        breakfastinterval= ItemAvailable()
        checkbreakfast=breakfastinterval.breakfast
        assert checkbreakfast==True, "The item entered is in breakfast time interval 6am to 11am"
#test 6
def test_lunch_item():
        lunchinterval= ItemAvailable()
        checklunch=lunchinterval.lunch
        assert checklunch==True, "The item entered is in lunch time interval 11am to 3pm"
#test 7
def test_dinner_item():
        dinnerinterval= ItemAvailable()
        checkdinner=dinnerinterval.dinner
        assert checkdinner==True, "The item entered is in dinner time interval 3pm to 9pm"
#test 8
def test_brunch_item():
        brunchinterval= ItemAvailable()
        checkbrunch=brunchinterval.brunch
        assert checkbrunch==True, "The item entered is in brunch time interval 6am to 3pm"
#test 9
def test_allday_item():
    alldayinterval = ItemAvailable()
    checkallday = alldayinterval.allday
    assert checkallday == True, "The item entered is in allday interval"
#test 10
def test_profile_info_valid():
        valid_info = [
            "name",
            "email",
            "phone",
        ]
        check_info = CustomerProfile()
        for info in valid_info:
            assert check_info.verify_info(info)== True, "All user profile info entered correctly"
#test 11
def test_valid_login():
    login = CustomerProfile()
    checklogin = login.invalidate_login()
    assert checklogin == True, "The login info entered ok"

#test 12
def test_profile_valid_order():
        valid_order = [
            "single",
            "multiple",
            "empty",
        ]
        check_order = OrdersItems()
        for info in valid_order:
            assert check_order.verify_order(info) == True, "Single, multi and no items orders are handled correctly"
#test 13
def test_valid_tip():
    tip = OrdersItems()
    checktip = tip.verify_tip()
    assert checktip == True, "The tip info entered ok"

#test 14
def test_add_remove_item():
        item_action = [
            "add",
            "remove",
        ]
        check_status = MenuItem()
        for name in item_action:
            assert check_status.verify_status(name) == True, "Add and remove items work ok"
#test 15
def test_delivery_fee():
        fee = DeliveryFee()
        checkfee = fee.added
        assert checkfee == True, "The delivery fee is added to the order"

