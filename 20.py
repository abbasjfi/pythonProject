numbers = []
while True:
    number = int(input("Enter Number: "))
    if number == 0:
        break
    numbers.append(number)

print(numbers)

total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)

count=len(numbers)
avg=total/count
print(avg)