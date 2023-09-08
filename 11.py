numbers = []

for i in range(5):
    num = int(input("لطفاً یک عدد وارد کنید: "))
    numbers.append(num)

    if num > 1:
        for j in range(2, num):
            if (num % j) == 0:
                print(num, "عدد اول نیست")
                break
        else:
            print(num, "عدد اول است")

print(numbers)