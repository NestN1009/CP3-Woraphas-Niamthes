def vatCalculate(totalPrice):
    result = totalPrice + totalPrice*7/100
    result = int(result)
    return result

totalPrice = float(input())

print(vatCalculate(totalPrice))