class OrdersItems:
    def __init__(self):
        self.single = True
        self.multiple= True
        self.empty = 1.5
    def verify_order(self,info):
        return True
    def verify_tip(self):
        return True
  #  def invalidate_item(self):
   #     self.valid = False
#
#Finalize order - single item	Finalize order with one item	customer prompted to enter payment method	please enter payment method
#Finalize order - Multiple Items	Finalize order - Multiple Items	customer prompted to enter payment method	please enter payment method
#Finalize order - No items