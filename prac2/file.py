out_file = open("name.txt", "w")
name = input("name:")
print(name, out_file.write(name))
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

out_file = open("number.txt", "w")
num1 = 17
num2 = 42
num3 = 400
print(num1, out_file.write(str(num1)))
print(num2, out_file.write(str(num2)))
print(num3, out_file.write(str(num3)))
out_file.close()

in_file = open("number.txt", "r")
number1 = int(in_file.readline(2))
number2 = int(in_file.readline(2))
in_file.close()
print(number1 + number2)