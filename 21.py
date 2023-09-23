name_list = []
while True:
    name = str(input("Enter name:"))
    if name == "exit":
        break
    name_list.append(name)
c = len(name_list)
sum = 0
for i in range(0, c, 1):
    sum = sum + len(name_list[i])

print(sum)
