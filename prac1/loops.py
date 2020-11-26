def main():
    for i in range(0, 101, 10):
        print(i, end="")
    print()

    for i in range(20, 0, -1):
        print(i, end="")
    print()

    star_num = int(input("Number of stars:"))
    while star_num > 0:
        star_num = star_num - 1
        print("*", end="")
    print()

    star_num = int(input("Number of stars:"))
    for i in range(1, star_num+1):
        print("*"*i)
    print()


main()