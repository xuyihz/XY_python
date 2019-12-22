import ex33_drill_fun
ex33_drill_fun.printNumber(6,1)

# rewrite ex33.py in for, range
i = 0
numbers = []

for i in range(6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1  # i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
