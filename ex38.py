ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop: Remove and return item at index (default last).
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])  # list start at 0
print(stuff[-1])  # whoa! fancy  -1 means the last one.
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:5]))  # super stellar！ [3:5] == 3 & 4
# The string whose method is called is inserted in between
# each given string. The result is returned as a new string.
# Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'