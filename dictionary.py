done = False
fruits = {}
while not done:
    m = input("enter a fruit, or press enter to quit")
    if m == "":
        done = True
    else:
        print("you typed:", m)
        if m in fruits:
            fruits[m] += 1
        else:
            fruits[m] = 1
    print(fruits)

