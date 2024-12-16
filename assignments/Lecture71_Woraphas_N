menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice = totalPrice + int(priceList[number])
    print(totalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)

showBill()
