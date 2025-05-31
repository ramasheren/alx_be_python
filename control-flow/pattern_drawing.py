size = int(input("Enter the size of the pattern: "))
line = 0
while line < size:
    count = 0
    while count < size:
        print("*", end="")
        count += 1
    print()
    line+=1