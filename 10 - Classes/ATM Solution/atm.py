class ATM():
    """This class provides a way to store bank name and withdarw money from given client balance"""

    def __init__ (self, balance, name):
        self.name = name
        self.balance = balance

    def give(self, request, amount):
        print ("give " + str(amount))
        return request - amount

    def do_request(self, request):
        self.balance -= request

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

Balance1 = 500
Balance2 = 1000

ATM1 = ATM(Balance1, "Smart Bank")
ATM2 = ATM(Balance2, "Baraka Bank")

ATM1.withdraw(277)
ATM1.withdraw(800)

ATM2.withdraw(100)
ATM2.withdraw(2000)