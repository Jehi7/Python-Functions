def checkNumbers(numbers):
    evenNumbers = []
    oddNumbers = []
    
    for i in numbers:
        if(i % 2 == 0):
            evenNumbers.append(i)
        else:
            oddNumbers.append(i)
        
    evenString = str(evenNumbers).replace("[", "").replace("]", "")
    oddString = str(oddNumbers).replace("[", "").replace("]", "")
    print(f"Os números pares são: {evenString}!")
    print(f"Os números impares são: {oddString}!")


