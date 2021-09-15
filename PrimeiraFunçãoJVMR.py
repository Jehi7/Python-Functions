def returnList(list, number):
    if(len(list) < number):
        print("Alerta: essa lista possui menos elementos que o número exigido!")
        return

    for i in list:
        if(list.index(i) <= number - 1):
            print(i)