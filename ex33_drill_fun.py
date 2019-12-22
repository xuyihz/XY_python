def printNumber(NumEnd, interval):

    i = 0
    numbers = []
    while i < NumEnd:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + interval  # i += interval
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)
