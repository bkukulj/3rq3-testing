from dinnerisserved.visatest import VisaTest
from dinnerisserved.itemavailabilitytest import ItemAvailable
from dinnerisserved.customerprofiletest import CustomerProfile
from dinnerisserved.itemsorderstest import OrdersItems
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


















#Select tip amount 5%	Select tip amount 5% (order total $50)	5% added to order total $52.5	order total $52.5
#Select tip amount 10%	Select tip amount 10% (order total $50)	10% added to order total $55	order total $55
#Finalize order without tip	Finalize order without tip (order total $50)	order total remains the same - $50	order total $50
#Select tip amount 5$	Select tip amount $5 (order total $50)	$5 added to order total - $55	order total $55
#Select tip amount 10$	Select tip amount $10 (order total $50)	$10 added to order total - $60	order total $60
#Select take-out option	Select take-out option (order total $50)	take out option selected, no delivery fee added	order total $50
#Select delivery option	select delivery option (order total $50)	delivery option selected, delivery fee added	order total $55
#Add delivery fee	add $5 to order total (order total $50)	$5 added to order total - $55	order total $55
#Delete orders	try deleting a placed order	order deleted successfully	order deleted
#Add items to the menu	test adding items to the menu	items added from the menu	item added to the menu
#Delete items from the menu	test deleting items to the menu	items deleted from the menu	item deleted from the menu
