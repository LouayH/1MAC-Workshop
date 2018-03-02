def give(request, amount):
    print ("give " + str(amount))
    return request - amount


def give_me_money(money, request):
    if (not isinstance(money, int) or not isinstance(request, int)):
        print ("Inputs must be numbers")
    elif (request < 0):
        print ("Request must be greater than 0")
    elif (request > money):
        print ("You don't have enough funds")
    else:
        while (request > 0):
            if (request >= 100):
                request = give(request, 100)
            elif (request >= 50):
                request = give(request, 50)
            elif (request >= 10):
                request = give(request, 10)
            elif (request >= 5):
                request = give(request, 5)
            elif (request >= 0):
                request = give(request, request)


money = 500
request = 274
give_me_money(money, request)