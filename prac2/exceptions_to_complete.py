finished = False
result = 0
while not finished:
    try:
        result=float(input("NUMBER: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)