product_list = []

while True:
    print("1)Add product")
    print("2)Print All product")
    print("3)Find By product name")
    print("4)Find By product price")
    print("0)Exit")

    option = int(input("Enter Option Numbers: "))

    if option == 1:
        print("ADD")
        product_name = input("Enter name: ")
        product_price = input("Enter price: ")
        product = [product_name, product_price]
        product_list.append(product)
        print("\nProduct Added")


    elif option == 2:
        print("Plase Waite")
        for p in product_list:
            print("product name ", p[0])
            print("product price :", p[1])
            print("-" * 50)

    # elif option == 3:
    #     print("Plase Waite")
    #     product_name = input("Enter product name to Search : ")
    #     for p in product_list:
    #         if p[0] == product_name:
    #             print("product name :", p[0])
    #             print("product price  :", p[1])
    #             print("-" * 50)
    elif option == 3:
        print("Plase Wait")
        product_name = input("Enter product name to Search: ")
        count = 0
        for p in product_list:
            if p[0] == product_name:
                print("Product name:", p[0])
                print("Product price:", p[1])
                print("-" * 50)
                count += 1

        print("Total products found:", count)


    #
    # elif option == 4:
    #     print("Plase Waite")
    #     phone = input("Enter product price to Search : ")
    #     for p in product_list:
    #         if p[1] == product_list:
    #             print("product name :", p[0])
    #             print("product price  :", p[1])
    #             print("-" * 50)
    elif option == 4:
        print("Plase Wait")
        product_price = input("Enter product price to Search: ")
        count = 0
        for p in product_list:
            if p[1] == product_price:
                print("Product name:", p[0])
                print("Product price:", p[1])
                print("-" * 50)
                count += 1

        print("Total products found:", count)


    elif option == 0:
        if (input("Are you sure (y/n) ?") == "y"):
            print("EXIT")
            break
    else:
        print("INVALID")

    input("\npress enter to continue")
