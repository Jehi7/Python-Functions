def turnNumberIntoBase5(x):
    if(x % 5 == 0):
        return(x)

    xPlus = x
    xMinus = x

    for i in range(0, 5):
        xPlus += 1
        xMinus -= 1

        if(xPlus % 5 == 0):
            return(xPlus)
        elif(xMinus % 5 == 0):
            return(xMinus)
   