inputresult = int(input("Írjon be egy szöveget!"))
print(f"Amit beírtál: {inputresult}")

print(type(inputresult))
print(isinstance(inputresult, int))

if not (isinstance(inputresult, int)):
    raise TypeError("Nem szám amit beírtál")