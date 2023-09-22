numbers = []

for i in range(100, 201, 1):
    numbers.append(i)

for number in numbers:
    is_prime = True
    for j in range(2, number):
        if (number % j) == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "عدد اول است")