def give(request, amount):
    print ("give " + str(amount))
    return request - amount

def do_request(balance, request):
    balance -= request

    amounts = [100, 50, 10, 5, 1]
    while (request > 0):
        for amount in amounts:
            if (request >= amount):
                if amount == 1:
                    amount = request
                request = give(request, amount)
                break
    return balance

def withdraw(balance, request):
    if (not isinstance(balance, int) or not isinstance(request, int)):
        print ("Inputs must be numbers")
    elif (request <= 0):
        print ("Request must be greater than 0")
    elif (request > balance):
        print ("You don't have enough funds")
    else:
        return do_request(balance, request)

balance = 500
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)

print ("Your balance: " + str(balance))