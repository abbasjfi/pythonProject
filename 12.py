numbers = []

while True:
    num = int(input("عدد را وارد کنید (برای خروج عدد 0 را وارد کنید): "))
    if num == 0:
        break
    numbers.append(num)

sum = sum(numbers)
avg = sum / len(numbers)

print("مجموع اعداد: ", sum)
print("میانگین اعداد: ", avg)
