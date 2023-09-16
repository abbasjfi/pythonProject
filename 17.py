import os

contact_list = []

while True:
    os.system("cls")
    print("1)Add Contact")
    print("2)Print All Contacts")
    print("3)Find By Family")
    print("4)Find By Phone")
    print("0)Exit")

    option = int(input("Enter Option : "))

    os.system("cls")

    if option == 1:
        print("ADD")
        family = input("Enter Family : ")
        phone = input("Enter Phone Number : ")

        for c in contact_list:
            if c[1] == phone:
                print("Duplicate Number !!!")
                break
        else:
            contact = [family, phone]
            contact_list.append(contact)
            print("\nContact Saved")

    elif option == 2:
        print("PRINT ALL")
        for c in contact_list:
            print("Family :", c[0])
            print("Phone  :", c[1])
            print("-" * 50)

    elif option == 3:
        print("FIND BY FAMILY\n")
        family = input("Enter Family to Search : ")
        for c in contact_list:
            if c[0] == family:
                print("Family :", c[0])
                print("Phone  :", c[1])
                print("-" * 50)

    elif option == 4:
        print("FIND BY PHONE\n")
        phone = input("Enter Phone to Search : ")
        sm = 0
        for p in contact_list:
            sm = sm + p[1]


    elif option == 0:
        if (input("Are you sure (y/n) ?") == "y"):
            print("EXIT")
            break
    else:
        print("INVALID")

    input("\npress enter to continue")
