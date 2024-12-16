menuList = []

def showBill():
    totalPrice = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],end=" ")
        print(menuList[number][1])

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("price :")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()
