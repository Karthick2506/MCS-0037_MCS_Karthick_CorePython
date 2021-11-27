class hotel:
    # State
    def __init__(self, orderid, tableno, foodname):
        self.orderid = orderid
        self.tableno = tableno
        self.foodname = foodname
    # Behaviour
    def get_order_details(self):
        print("The Order Details:")
        print("The Order id:", self.orderid, "Table No:", self.tableno, "Food:", self.foodname)


order = hotel(3452, 10, "Chicken Pizza")
order.get_order_details()