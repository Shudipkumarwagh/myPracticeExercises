# pattern writing program take the 2 input from user for how many line to print nd in which order ascending and
# descending order input take it into boolean variable and if it is true then print the pattern into ascending order
# else descending order

print("Enter the number of lines you want to print:")
numLine = int(input())
print("How to print the order 1 ascending and 0 for descending")
myOpt = bool(int(input()))
mynum = 0

if myOpt:
    print("Ascending Pattern")
    for mynum in range(numLine + 1):
        # while mynum <= numLine:
        for i in range(mynum):
            print("*", end=" ")
        print()
        # mynum += 1
else:
    # for num in range()
    while numLine > 0:
        for i in range(numLine):
            print("*", end=" ")
        print()
        numLine -= 1
