while True:
    try:
        x = int(input("Please enter a number: "))
        if x < 10:
            raise ValueError()
        break
    except ValueError:
        print("Oops, that was not a valid number. Try again...")