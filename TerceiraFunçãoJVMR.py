def Greetings(name, age):
    firstName = name.split(" ")[0]
    fmt = "Olá {0}! Parabéns, você tem {1} anos!"

    print(fmt.format(firstName, age))