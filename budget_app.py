class Category:

    def __init__(self, category):
        """Create an Instance of class."""
        self.category = category
        self.ledger = []
        self.balance = 0
        self.spent = 0
    
    def deposit(self, amount, description=""):
        """This Function Accepts the deposits and a description."""
        dep_dict = {
            "amount": amount,
            "description": description
        }
        self.balance += dep_dict["amount"]
        self.ledger.append(dep_dict)

    def withdraw(self, amount, description=""):
        """This function withdraw the amount."""
        with_dict = {
            "amount": -amount,
            "description": description
        }
        if amount <= self.balance:
            self.balance -= amount
            self.spent += amount
            self.ledger.append(with_dict)
            return True
        else: return False
    
    def get_balance(self):
        """This Function will return the current balance."""
        return self.balance

    def transfer(self, amount, transfer_to):
        """This function will accept from or make transfer to another category."""
        process_transfer_from = f"Transfer from {self.category}"
        process_transfer_to = f"Transfer to {transfer_to.category}"
        send_dict = {"amount": -amount, "description": process_transfer_to}
        recv_dict = {"amount": amount, "description": process_transfer_from}
        if amount <= self.balance:
            self.balance -= amount
            transfer_to.balance += amount
            self.ledger.append(send_dict)
            transfer_to.ledger.append(recv_dict)
            return True
        else: return False
    
    def check_funds(self, amount):
        """
        This function will check if you have enough balance as
        amount(argument).
        """
        if amount > self.balance:
            return False
        return True
    
    def budget(self):
        """This function will show descriptive transactions and total."""
        print_category = self.category
        print_total = self.balance
        header = print_category.center(30, '*')
        left = ''
        right = ''
        show = header
        length = 0
        for transactions in self.ledger:
            left = transactions["description"][:23]
            length = len(left)
            right = "{0:.2f}".format(transactions["amount"])
            right = str(right).rjust(30 - length)
            final_str = "\n" + left + right
            show += final_str
        show += "\nTotal: " + str(print_total)
        return show
    
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

# ALL TEST PASSED.
# food.deposit(900, "deposit")
# print(food.ledger[0])  # OK.
# food.deposit(45.56)
# print(food.ledger[0])  # OK.
# food.deposit(900, 'deposit')
# food.withdraw(45.76, "milk, cereal, eggs, bacon, bread")
# print(food.ledger[1])  # OK.
# food.deposit(900, "deposit")
# food.withdraw(45.67)
# print(food.ledger[1])
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.get_balance()  # OK.
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food.get_balance()
# entertainment.get_balance()
# food.transfer(transfer_amount, entertainment)
# food.get_balance()
# entertainment.get_balance()
# print(food.ledger[2])
# print(entertainment.ledger[0])  # OK.
# food.deposit(10, "deposit")
# print(food.check_funds(20))
# food.deposit(10)
# print(food.check_funds(20))
# food.deposit(100, "deposit")
# print(food.withdraw(100))  # OK.
# food.deposit(100, "deposit")
# print(food.transfer(200, entertainment))  # OK.
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# s = food.budget()
# print(s)  # OK.