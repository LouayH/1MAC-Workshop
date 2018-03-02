class ATM():
    """This class provides a way to store bank name and withdarw money from given client balance"""

    def __init__ (self, balance, name):
        self.name = name
        self.balance = balance
        self.withdrawals = []

    def give(self, request, amount):
        print ("give " + str(amount))
        return request - amount

    def do_request(self, request):
        self.balance -= request
        self.withdrawals.append(request)

        amounts = [100, 50, 10, 5, 1]
        while (request > 0):
            for amount in amounts:
                if (request >= amount):
                    if amount == 1:
                        amount = request
                    request = self.give(request, amount)
                    break

        print ("=" * 30)
        return self.balance

    def withdraw(self, request):
        print ("Welcome to " + self.name)
        print ("Current Balance = " + str(self.balance))
        print ("-" * 30)
        if (not isinstance(self.balance, int) or not isinstance(request, int)):
            print ("Inputs must be numbers")
        elif (request <= 0):
            print ("Request must be greater than 0")
        elif (request > self.balance):
            print ("You don't have enough funds")
        else:
            return self.do_request(request)

    def show_withdrawals(self):
        print ("Welcome to " + self.name)
        print("-" * 30)
        number = 1
        for withdrawal in self.withdrawals:
            print ("Withdrawal {0}: {1}".format(number, withdrawal))
            number += 1
        print("-" * 30)
        print("Current Balance = " + str(self.balance))
        print("=" * 30)

Balance = 500

ATM = ATM(Balance, "Smart Bank")

ATM.withdraw(150)
ATM.withdraw(75)
ATM.withdraw(225)

ATM.show_withdrawals()