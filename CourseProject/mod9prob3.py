


numbers = []
total = 0

while total <= 100:
    num = float(input("Enter a number: "))
    numbers.append(num)
    total += num

print("Numbers entered:", numbers)
print("Sum of numbers:", total)