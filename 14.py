
for num in range(10, 100, 1):
    if num > 1:
        for j in range(2, num):
            if (num % j) == 0:
                print(num, "عدد اول نیست")
                break
        else:
            print(num, "عدد اول است")
