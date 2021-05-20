def ly(n):
    if (type(n) != int):
        print("Error: invalid input, ints only.")

    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            print(n, "is not a leap year")
        else:
            print(n, "is a leap year")
    else:
        print(n, "is not a leap year")