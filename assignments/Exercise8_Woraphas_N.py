usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "genPhys" and passwordInput == "skibidi":
    print("done !")
    print("Welcome to myStore")
    print("Product : 1     10 $")
    print("Product : 2     100 $")
    print("Product : 3     1000 $")

    chooseProduct1 = int(input("Choose your the first product which you want(input number 1,2 or 3 only) : "))
    if chooseProduct1 == 1:
        print("Your product price is 10$")
        price1 = 10
    elif chooseProduct1 == 2:
        print("Your product price is 100$")
        price1 = 10
    elif chooseProduct1 == 3:
        print("Your product price is 1000$")
        price1 = 10
    print("Now, your summary price = ",price1," $")

    answer = input("Do you want to choose the second product ? :")
    if answer == "yes":
        chooseProduct2 = int(input("Choose your the second product which you want(input number 1,2 or 3 only) : "))
        if chooseProduct2 == 1:
            print("Your product price is 10$")
            price2 = 10
        elif chooseProduct2 == 2:
            print("Your product price is 100$")
            price2 = 100
        elif chooseProduct2 == 3:
            print("Your product price is 1000$")
            price2 = 1000
        print("Now, your summary price = ", price1 + price2, " $")
        answer = input("Do you want to choose the third product ? :")
        if answer == "yes":
            chooseProduct3 = int(input("Choose your the second product which you want(input number 1,2 or 3 only) : "))
            if chooseProduct3 == 1:
                print("Your product price is 10$")
                price3 = 10
            elif chooseProduct3 == 2:
                print("Your product price is 100$")
                price3 = 100
            elif chooseProduct3 == 3:
                print("Your product price is 1000$")
                price3 = 1000
            print("Now, your summary price = ", price1 + price2 + price3, " $")
        elif answer == "no":
            chooseProduct3 = "Not choose"
            price3 = 0
            print("Let's go to checkout")
    elif answer == "no":
        chooseProduct2 = "Not choose"
        price2 = 0
        print("Let's go to checkout")

    print("Receipt")
    print("Product: ",chooseProduct1," ",price1,"$")
    print("Product: ", chooseProduct2, " ", price2,"$")
    print("Product: ", chooseProduct3, " ", price3,"$")
    print("All",price1+price2+price3,"$")

else:
    print("Your username or password not correct")