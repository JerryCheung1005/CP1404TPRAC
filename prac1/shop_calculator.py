def main():
    num = int(input('Number of items:'))

    sum_price = 0
    i = 0
    while i < num:
        price = float(input('Price of item:'))
        i += 1
        sum_price = sum_price + price

    if sum_price > 100:
        print('Total price for {0} items is: {1}'.format(num, sum_price * 0.9))
    elif 0 < sum_price < 100:
        print('Total price for {0} items is: {1}'.format(num, sum_price))

main()